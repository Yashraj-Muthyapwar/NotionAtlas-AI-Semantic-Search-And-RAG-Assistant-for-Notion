
# Notion RAG Pipeline Project

This project demonstrates an end-to-end Retrieval Augmented Generation (RAG) pipeline leveraging Notion content, sentence transformers for embeddings, Qdrant vector database, and Streamlit for real-time chat interaction.

## 📂 Project Structure

```
NotionRAG-Project/
├── DatabaseExtractor.py        # Extract Notion workspace pages, save to file
├── NotionRAG.ipynb             # Sentence embedding creation and Qdrant ingestion
├── StreamlitApp.py             # Interactive chat app using Streamlit + Ngrok
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation
```

## 🚀 Usage Instructions

### 1. Notion Data Extraction
```bash
python DatabaseExtractor.py
```
Extracts structured Notion content to a local JSON/text file.

### 2. Generate Embeddings & Upload to Qdrant
Run the notebook:
```bash
NotionRAG.ipynb
```
Creates sentence-level embeddings and stores them in Qdrant.

### 3. Launch Streamlit Demo
```bash
python StreamlitApp.py
```
Access your real-time chat interface with Qdrant-powered retrieval and LLaMA or OpenAI responses.

## 🛠 Dependencies

Install dependencies with:
```bash
pip install -r requirements.txt
```

### requirements.txt Example:
```
notion-client
qdrant-client
sentence-transformers
streamlit
pyngrok
requests
```

## 🌐 Notes
- Ensure your Notion API token and database/page IDs are properly configured.
- Update Qdrant host, collection name, and API keys as needed.
- LLaMA or OpenAI credentials required for chatbot responses.

## 💡 Future Improvements
- Recursive subpage handling
- Automated chunking and batch upserts
- Dockerized deployment

---

Contributions welcome. Built with ❤️ for private RAG pipelines.
