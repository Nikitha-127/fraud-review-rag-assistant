# app/vector_store.py

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


def load_vector_store():
    return FAISS.load_local(
        "vector_db/faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )
