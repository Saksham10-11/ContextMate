from langchain_community.llms.ollama import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores.chroma import Chroma
from embedder import get_embedding_function
from dotenv import load_dotenv
import os

load_dotenv()
chroma_directory = os.getenv("CHROMA_DIRECTORY")

template = '''
Answer the questions below based on the following context : {context}

Here's the conversation history : {history}

Question : {question}

Answer : 
'''

chromaDB = Chroma(persist_directory=chroma_directory,embedding_function=get_embedding_function())

def get_relevant_context(query):
    results = chromaDB.similarity_search_with_score(query,k=2)
    context_text = "\n\n --- \n\n".join([doc.page_content for doc,_score in results])
    return context_text

def run():
    model = Ollama(model="llama3.2")
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    history = ""
    print("Welcome to the AI chatbot! Type 'exit' to quit.")
    while True:
        user_input = input('user : ')
        context = get_relevant_context(user_input)
        if user_input.lower()=='exit':
            break
        result = chain.invoke({"context":context,"history":history,"question":user_input})
        print("Bot : ",result)
        history += f"User : {user_input}\nAI : {result}\n"

if __name__ == '__main__':
    run()