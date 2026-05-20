# app/rag_service.py

from transformers import pipeline
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load free local embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS vector DB
vectorstore = FAISS.load_local(
    "vector_db/faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# Free HuggingFace text generation model
generator = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)


def query_rag(question: str, top_k: int = 4):

    docs = vectorstore.similarity_search(question, k=top_k)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    You are a fraud review assistant.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    result = generator(
        prompt,
        max_length=256,
        do_sample=False
    )

    answer = result[0]["generated_text"]

    return {
        "question": question,
        "answer": answer,
        "sources": [doc.page_content for doc in docs]
    }
