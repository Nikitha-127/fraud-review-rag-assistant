# Fraud Review Assistant | RAG + FastAPI + LangChain

A production-style Retrieval-Augmented Generation project that helps fraud analysts search internal fraud policies, compliance guidelines, and transaction scenarios. The assistant retrieves relevant evidence and generates audit-friendly review guidance.

## Features

- FastAPI backend with `/health`, `/ingest`, and `/query` endpoints
- LangChain-based RAG pipeline
- FAISS local vector database for easy local execution
- OpenAI embeddings and chat model support
- Sample fraud policy, compliance, and transaction documents
- Source-backed responses for analyst review
- GitHub-ready structure with tests and documentation

## Tech Stack

- Python
- FastAPI
- LangChain
- FAISS
- OpenAI API
- Pydantic
- Uvicorn
- Pytest

## Project Structure

```text
fraud-review-assistant/
├── app/
│   ├── config.py
│   ├── document_loader.py
│   ├── main.py
│   ├── rag_service.py
│   ├── schemas.py
│   └── vector_store.py
├── data/
│   ├── compliance_guidelines.txt
│   ├── fraud_policy.txt
│   └── sample_transactions.txt
├── tests/
│   └── test_health.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/fraud-review-assistant.git
cd fraud-review-assistant
```

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
# .venv\Scripts\activate    # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

```bash
cp .env.example .env
```

Add your OpenAI API key:

```text
OPENAI_API_KEY=your_api_key_here
```

### 5. Run the API

```bash
uvicorn app.main:app --reload
```

Open API docs:

```text
http://127.0.0.1:8000/docs
```

## Usage

### Ingest documents

```bash
curl -X POST http://127.0.0.1:8000/ingest
```

### Ask a fraud review question

```bash
curl -X POST http://127.0.0.1:8000/query \
  -H "Content-Type: application/json" \
  -d '{
    "question": "A customer added a new beneficiary and made three international transfers from a new device. What should the analyst do?",
    "top_k": 4
  }'
```

## Example Questions

- What should an analyst do if a password reset is followed by a high-value transfer?
- When should a case be escalated for suspected account takeover?
- What evidence should be documented in a fraud decision?
- How should sensitive customer information be handled during AI-assisted review?

## Resume Description

**Fraud Review Assistant | RAG + FastAPI + LangChain**  
Built a retrieval-augmented AI assistant to support fraud investigation and compliance workflows. Developed semantic search and document retrieval pipelines using LangChain, FAISS/Pinecone-ready architecture, and FastAPI to improve access to transaction and policy-related information.

## Future Improvements

- Add Pinecone cloud vector database support
- Add authentication with JWT/OAuth2
- Add analyst feedback collection
- Add Streamlit or React frontend
- Add evaluation tests for answer faithfulness and retrieval quality
- Add Dockerfile and cloud deployment pipeline
