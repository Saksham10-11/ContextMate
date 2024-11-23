from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.document import Document
from dotenv import load_dotenv
import os

def load_documents(DIR_PATH : str):
    documents = []
    for root,dir,file in os.walk(DIR_PATH):
        for filename in file:
            path = os.path.join(root,filename)
            if filename.endswith('.pdf'):
                loader = PyPDFLoader(path,extract_images=True)
                document = loader.load_and_split()
                documents.extend(document)
    return documents


def split_documents(documents : list[Document]):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 600,
        chunk_overlap = 80,
        length_function = len,
        is_separator_regex = False
    )
    return splitter.split_documents(documents)

