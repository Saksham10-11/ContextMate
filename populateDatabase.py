from langchain_community.vectorstores.chroma import Chroma
from documentLoader import load_documents,split_documents
from embedder import get_embedding_function
from dotenv import load_dotenv
import shutil
import os

load_dotenv()
chroma_directory = os.getenv("CHROMA_DIRECTORY")
DIR_PATH = os.getenv("DIRECTORY_PATH")

def prepare_chunks():
    documents = load_documents(DIR_PATH)
    print("Done loading documents...")
    chunks = split_documents(documents)
    print("Done creating chunks...")
    return chunks

def add_to_chromaDB():
    chunks = prepare_chunks()
    chromaDB = Chroma(persist_directory=chroma_directory,embedding_function=get_embedding_function())

    chunks_with_ids = calculate_chunk_ids(chunks)
    
    existing_items = chromaDB.get(include=[])
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")
    
    # Only add documents that don't exist in the DB.
    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks):
        print(f"👉 Adding new documents: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        chromaDB.add_documents(new_chunks, ids=new_chunk_ids)
    else:
        print("✅ No new documents to add")

def calculate_chunk_ids(chunks):
    last_page_id = None
    current_chunk_index = 0
    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id
        chunk.metadata["id"] = chunk_id
    return chunks

if __name__ == '__main__':
    add_to_chromaDB()