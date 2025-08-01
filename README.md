<h1 align="center">🚀 NotionAtlas — AI Semantic Search & RAG Assistant for Notion</h1>

<p align="center"><i>Transform your Notion workspace into an interactive, intelligent knowledge assistant — featuring Retrieval-Augmented Generation (RAG), semantic search, and real-time answers from powerful AI models.

---
</i></p>
<p align="center"><i>⚡️ Tech Stack</i></p>

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Qdrant-FF6F00?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHdpZHRoPScxNScgaGVpZ2h0PScxNScgdmlld0JveD0nMCAwIDMyIDMyJz48cGF0aCBkPSdNMCAxNiBDMCA3LjE2NiA3LjE2NiAwIDE2IDBDMjQuODM0IDAgMzIgNy4xNjYgMzIgMTYgQzMyIDI0LjgzNCAyNC44MzQgMzIgMTYgMzIgQzcuMTY2IDMyIDAgMjQuODM0IDAgMTYgeicgZmlsbD0nI2ZmZicvPjwvc3ZnPg==&logoColor=white" alt="Qdrant">
  <img src="https://img.shields.io/badge/LLaMA-FF0080?logo=llama&logoColor=white" alt="LLaMA">
  <img src="https://img.shields.io/badge/NotionAPI-000000?logo=notion&logoColor=white" alt="Notion API">
  <img src="https://img.shields.io/badge/HuggingFace-FEDC56?logo=huggingface&logoColor=black" alt="Hugging Face">
</p>

---
## 📖 Overview

**NotionAtlas** is an end-to-end AI toolkit that turns your Notion workspace into a smart, conversational, and context-aware knowledge base. It combines best-in-class semantic search with state-of-the-art LLMs (like Llama 4) to deliver accurate, grounded answers — all through a modern Streamlit interface.

- **End-to-End RAG Workflow:** Automates extraction, chunking, embedding, retrieval, and generation over your Notion content.
- **AI-Powered Q&A:** Seamlessly blends semantic search and large language models for instant, context-rich answers.
- **User-Friendly Interface:** Engage with your Notion knowledge through an intuitive chat app, accessible from any browser.

---

<img width="810" height="449" alt="neuronotion" src="https://github.com/user-attachments/assets/74cd5062-c1ca-4e4b-a82a-240d120fea3b" />




## ✨ Features

- 🍀 **Automatic Notion Extraction:** Pulls and structures content directly from Notion using its API.
- 🔍 **Semantic Search & Smart Chunking:** Indexes your workspace into fine-grained, searchable chunks (flashcards, paragraphs, Q&A).
- 🤖 **RAG (Retrieval-Augmented Generation):** Retrieves the most relevant Notion context and augments LLM answers for accuracy and trust.
- 🧠 **Real-Time Conversational Q&A:** Ask anything, get instant, context-aware responses. Supports flashcard drill-down and deep search.
- ⚡ **Production-Ready & Configurable:** Modular design, secure API key handling, and one-click deploy.
- 🛡️ **Privacy First:** Only relevant Notion snippets are sent to the AI for answering; your data stays safe.

---
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
- **LLaMA** credentials required for chatbot responses.
- **Huggingface** token for sentence-transformers
- Update the credentials in your environment or config files before running.

---

Contributions welcome. Built with ❤️ for modern knowledge management and AI innovation.
