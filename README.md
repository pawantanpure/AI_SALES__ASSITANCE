# AI_Sales_Assitance

An intelligent AI-powered Sales Assistant built using **Llama 3, LangChain, ChromaDB, Hugging Face Embeddings, and Streamlit**. The application enables sales teams to upload business documents, perform semantic search, generate contextual answers, prepare for meetings, analyze competitors, and handle customer objections using Retrieval-Augmented Generation (RAG).

---

## Features

### Document Upload & Processing

* Upload PDF sales documents
* Automatic text extraction and chunking
* Embedding generation using Sentence Transformers
* Persistent vector storage with ChromaDB

### Semantic Search

* Retrieve relevant information from uploaded documents
* Context-aware search using vector embeddings
* Faster access to sales knowledge

### AI-Powered Question Answering

* Retrieval-Augmented Generation (RAG)
* Contextual responses using Llama 3
* Reduces hallucinations by grounding answers in source documents

### Meeting Preparation

* Generate meeting briefs
* Identify customer pain points
* Suggest discussion topics and questions

### Competitor Intelligence

* Compare products and services
* Highlight strengths and weaknesses
* Generate competitive insights

### Customer Objection Handling

* Handle common sales objections
* Generate persuasive and professional responses
* Improve sales conversations

---

## Tech Stack

### Frontend

* Streamlit

### Backend

* Python

### LLM

* Llama 3 (via Ollama)

### AI Framework

* LangChain

### Vector Database

* ChromaDB

### Embeddings

* Hugging Face Sentence Transformers
* all-MiniLM-L6-v2

### Document Processing

* PyPDFLoader
* RecursiveCharacterTextSplitter

---

## Project Architecture

PDF Documents
↓
Document Loader
↓
Text Chunking
↓
Embeddings
↓
ChromaDB Vector Store
↓
Retriever
↓
Llama 3
↓
AI Sales Assistant

---

## Folder Structure

```text
AI_Sales_Assistant/

├── app.py
├── requirements.txt
│
├── data/
│   └── uploads/
│
├── modules/
│   ├── rag.py
│   ├── meeting_prep.py
│   ├── competitor.py
│   └── objection.py
│
├── chroma_db/
│
└── assets/
```

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/AI_Sales_Assistant.git
cd AI_Sales_Assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama & Llama 3

Install Ollama from:

https://ollama.com

Pull Llama 3 model:

```bash
ollama pull llama3
```

Run model:

```bash
ollama run llama3
```

---

## Run Application

```bash
streamlit run app.py
```

---

## Example Questions

* What is relationship selling?
* What are the responsibilities of a sales manager?
* What are the benefits of customer relationship management?
* Summarize the uploaded sales document.
* Compare our product with competitors.

---

## Future Enhancements

* Multi-PDF support
* Chat history memory
* Source citations
* Sales analytics dashboard
* CRM integration
* PDF report generation
* Multi-model support (GPT, Claude, Gemini)
* Voice-enabled sales assistant

---

## Learning Outcomes

This project demonstrates:

* Retrieval-Augmented Generation (RAG)
* Large Language Models (LLMs)
* Semantic Search
* Vector Databases
* Prompt Engineering
* Document Intelligence
* LangChain Framework
* Streamlit Application Development
* Local LLM Deployment using Ollama

---

## Author

Pawan Dhiraj Tanpure

B.Tech | Full Stack Data Science 

Passionate about AI Engineering, Machine Learning, NLP, Agentic AI, and Large Language Models.
