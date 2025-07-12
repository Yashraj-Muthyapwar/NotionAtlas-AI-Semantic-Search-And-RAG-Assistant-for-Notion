<h1 align="center">NOTION-RAG-PIPELINE</h1>

<p align="center"><i>Transform Knowledge into Action Instantly</i></p>
<p align="center"><i>Built with the tools and technologies:</i></p>

<p align="center">
  <img src="https://img.shields.io/badge/Markdown-000000?logo=markdown&logoColor=white" alt="Markdown">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Qdrant-FF6F00?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPScxNScgaGVpZ2h0PScxNScgdmlld0JveD0nMCAwIDMyIDMyJz48cGF0aCBkPSdNMCAxNiBDMCA3LjE2NiA3LjE2NiAwIDE2IDBDMjQuODM0IDAgMzIgNy4xNjYgMzIgMTYgQzMyIDI0LjgzNCAyNC44MzQgMzIgMTYgMzIgQzcuMTY2IDMyIDAgMjQuODM0IDAgMTYgeicgZmlsbD0nI2ZmZicvPjwvc3ZnPg==&logoColor=white" alt="Qdrant">
  <img src="https://img.shields.io/badge/LLaMA-FF0080?logo=llama&logoColor=white" alt="LLaMA">
  <img src="https://img.shields.io/badge/NotionAPI-000000?logo=notion&logoColor=white" alt="Notion API">
  <img src="https://img.shields.io/badge/HuggingFace-FEDC56?logo=huggingface&logoColor=black" alt="Hugging Face">
</p>

---
## 📖 Overview

Notion-RAG-Pipeline is a developer-focused toolkit that transforms your Notion workspace into an intelligent, searchable knowledge base powered by AI. It streamlines data extraction, embedding, and retrieval, enabling seamless, real-time interactions within your Notion environment.

<img width="810" height="449" alt="neuronotion" src="https://github.com/user-attachments/assets/74cd5062-c1ca-4e4b-a82a-240d120fea3b" />




### Why Notion-RAG-Pipeline?

This project simplifies the process of building and deploying a knowledge retrieval system from Notion data. The core features include:

- 🍀🔍 **Content Extraction & Embedding:** Efficiently extracts and transforms Notion pages and databases into embeddings for fast retrieval.
- 🚀🌐 **Real-time AI Chat Interface:** Integrates a user-friendly Streamlit app for context-aware, AI-powered Q&A within Notion.
- 🧠🤖 **Retrieval-Augmented Generation:** Combines retrieval with language models to produce accurate, relevant responses.
- ⚙️ **Environment Consistency:** Uses a well-defined dependencies file for seamless setup across systems.
- 📊📄 **End-to-End Data Workflow:** Supports data ingestion, embedding, and interactive querying, streamlining knowledge management.

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


## 🌐 Notes
- Ensure your **Notion** API token and database/page IDs are properly configured.
- Update **Qdrant** host, collection name, and API keys as needed.
- **LLaMA/OpenAI** credentials required for chatbot responses.
- **Huggingface** token for sentence-transformers
- Update the credentials in your environment or config files before running.

## 💡 Future Improvements
- Recursive subpage handling
- Automated chunking and batch upserts
- Dockerized deployment

---

Contributions welcome. Built with ❤️ for private RAG pipelines.
