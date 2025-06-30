from notion_client import Client
import json

# Auth handled externally
notion = Client(auth="YOUR_NOTION_API_KEY_HERE")  # Replace with your actual Notion API key


class NotionExtractor:
    """Extracts structured Notion content, including hyperlinks, ready for Markdown or text processing."""

    def __init__(self, notion_client):
        self.notion = notion_client

    def extract_text(self, rich_text_array):
        """
        Extract plain text or markdown-formatted text with hyperlinks from rich_text arrays.
        """
        parts = []
        for item in rich_text_array:
            if "text" not in item:
                continue

            text_content = item["text"]["content"]
            link = item["text"].get("link")

            if link and link.get("url"):
                parts.append(f"[{text_content}]({link['url']})")
            else:
                parts.append(text_content)

        return "".join(parts)

    def extract_block(self, block, depth=0):
        results = []
        indent = "  " * depth
        block_type = block["type"]

        if block_type.startswith("heading_"):
            heading = self.extract_text(block[block_type]["rich_text"])
            heading_level = block_type.split("_")[1]
            results.append(f"{indent}{'#' * int(heading_level)} {heading}")

            if block.get(block_type, {}).get("is_toggleable", False) and block.get("has_children", False):
                results.extend(self.recursive_extract(block["id"], depth + 1))

        elif block_type == "paragraph":
            text = self.extract_text(block["paragraph"]["rich_text"])
            if text.strip():
                results.append(f"{indent}{text}")

        elif block_type == "bulleted_list_item":
            text = self.extract_text(block["bulleted_list_item"]["rich_text"])
            results.append(f"{indent}- {text}")
            if block.get("has_children", False):
                results.extend(self.recursive_extract(block["id"], depth + 1))

        elif block_type == "numbered_list_item":
            text = self.extract_text(block["numbered_list_item"]["rich_text"])
            results.append(f"{indent}1. {text}")
            if block.get("has_children", False):
                results.extend(self.recursive_extract(block["id"], depth + 1))

        elif block_type == "image":
            url = block["image"].get("file", {}).get("url") or block["image"].get("external", {}).get("url")
            results.append(f"{indent}![Image]({url})")

        elif block_type == "pdf":
            url = block["pdf"].get("file", {}).get("url") or block["pdf"].get("external", {}).get("url")
            results.append(f"{indent}[PDF Document]({url})")

        elif block_type == "file":
            url = block["file"].get("file", {}).get("url") or block["file"].get("external", {}).get("url")
            results.append(f"{indent}[File]({url})")

        elif block_type == "bookmark":
            url = block["bookmark"]["url"]
            results.append(f"{indent}[Bookmark]({url})")

        elif block_type == "code":
            code_text = self.extract_text(block["code"]["rich_text"])
            language = block["code"].get("language", "text")
            results.append(f"{indent}```{language}\n{code_text}\n```")

        elif block_type == "quote":
            quote_text = self.extract_text(block["quote"]["rich_text"])
            results.append(f'{indent}> {quote_text}')

        elif block_type == "callout":
            callout_text = self.extract_text(block["callout"]["rich_text"])
            emoji = block["callout"].get("icon", {}).get("emoji", "")
            results.append(f"{indent}💡 {emoji} {callout_text}")

        elif block_type == "toggle":
            toggle_text = self.extract_text(block["toggle"]["rich_text"])
            results.append(f"{indent}▶ {toggle_text}")
            if block.get("has_children", False):
                results.extend(self.recursive_extract(block["id"], depth + 1))

        return results

    def extract_database_pages(self, database_id):
        """
        Fetches all pages from a Notion database and extracts their content.

        :param database_id: The Notion database ID
        :return: Dictionary with {page_title: content_list}
        """
        results = {}

        response = self.notion.databases.query(database_id=database_id)

        for page in response.get("results", []):
            page_id = page["id"]
            properties = page.get("properties", {})

            # Try to get title from 'Title' property, fallback to Untitled
            title = "Untitled Page"
            for prop in properties.values():
                if prop.get("type") == "title":
                    title_text = self.extract_text(prop["title"])
                    if title_text.strip():
                        title = title_text
                    break

            content = self.recursive_extract(page_id)
            results[title] = content

        return results

    def recursive_extract(self, block_id, depth=0):
        results = []
        response = self.notion.blocks.children.list(block_id)

        for block in response["results"]:
            results.extend(self.extract_block(block, depth))

        return results

    def extract_page(self, page_id):
        return self.recursive_extract(page_id)


def extract_nested_database_to_json(notion_extractor, database_id):
    """
    Extract pages from a Notion database, their subpages, and content in RAG-friendly JSON format.
    """
    notion = notion_extractor.notion
    final_data = []

    # Query all top-level pages in the database
    response = notion.databases.query(database_id=database_id)

    for page in response.get("results", []):
        page_id = page["id"]
        properties = page.get("properties", {})

        # Extract title
        title = "Untitled Page"
        for prop in properties.values():
            if prop.get("type") == "title":
                title_text = notion_extractor.extract_text(prop["title"])
                if title_text.strip():
                    title = title_text
                break

        # Initialize record for this page
        page_record = {
            "page_id": page_id,
            "title": title,
            "subpages": []
        }

        # Fetch children blocks to find subpages
        child_blocks = notion.blocks.children.list(page_id).get("results", [])

        for block in child_blocks:
            if block["type"] == "child_page":
                subpage_id = block["id"]
                subpage_title = block["child_page"].get("title", "Untitled SubPage")

                # Extract subpage content
                subpage_content = notion_extractor.extract_page(subpage_id)
                full_text = "\n".join(subpage_content)

                page_record["subpages"].append({
                    "subpage_id": subpage_id,
                    "title": subpage_title,
                    "content": full_text
                })

        final_data.append(page_record)

    return final_data

# Auth & Init
extractor = NotionExtractor(notion)

# Database ID
database_id = "Your_Database_ID_Here"  # Replace with your actual Notion database ID

# Extract pages to JSON format
page_data = extract_nested_database_to_json(extractor, database_id)

# Preview as JSON
output = json.dumps(page_data, indent=2)
print(output)

# Save to file
with open("notion_database_output.txt", "w") as f:
    f.write(output)