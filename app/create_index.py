# app/create_index.py

import os

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

documents = []

data_folder = "data"

for file in os.listdir(data_folder):
    if file.endswith(".txt"):
        loader = TextLoader(os.path.join(data_folder, file))
        documents.extend(loader.load())

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(
    docs,
    embeddings
)

os.makedirs("vector_db/faiss_index", exist_ok=True)

vectorstore.save_local("vector_db/faiss_index")

print("FAISS index created successfully")
