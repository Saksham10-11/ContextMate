from langchain_community.embeddings.ollama import OllamaEmbeddings

def get_embedding_function():
    embedder = OllamaEmbeddings(model='nomic-embed-text')
    return embedder

if __name__ == '__main__':
    embedder = get_embedding_function()
    embeddings = embedder.embed_documents(["This is my first text to embed", "This is my second document"])
    print(embeddings)