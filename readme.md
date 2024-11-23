# Local Chatbot with Ollama & Chroma

This chatbot uses **Ollama's** `llama3.2` model and **Chroma** to help answer your questions based on documents stored locally. It retrieves relevant information from your files and generates responses in real time.

## Features

- **Ollama Integration**: Uses the powerful `llama3.2` model for human-like responses.
- **Chroma for Document Search**: Efficiently searches through document chunks to provide context for responses.
- **Runs Locally**: Everything is set up to run on your machine.

## Quick Setup

### 1. Install Dependencies

Make sure you have Python 3.7+ and then install required libraries:

```bash
pip install langchain langchain_community chromadb dotenv
```

### 2. Install Ollama

- Download and install **Ollama** from [here](https://ollama.com).
- Run the Ollama server locally:

```bash
ollama serve
```

### 3. Set Environment Variables

Create a `.env` file in your project folder with the following content:

```
CHROMA_DIRECTORY=path_to_your_chroma_directory
DIRECTORY_PATH=path_to_your_documents_directory
```

- `CHROMA_DIRECTORY`: Directory where Chroma will store its index.
- `DIRECTORY_PATH`: Directory where your documents (PDFs, texts) are stored.

### 4. Load Data

Before running the chatbot, you need to load and process your documents. This can be done by running the **populateDatabase.py** script:

```bash
python populateDatabase.py
```

This will load your documents into Chroma's vector store. After that, you can start the chatbot.

### 5. Run the Chatbot

Once your documents are loaded, simply run the chatbot:

```bash
python chatbot.py
```

The chatbot will prompt you to enter a question. Type your question, and it will generate an answer based on the context of your documents. Type `exit` to stop.

## How It Works

- **Data Loading**: The `populateDatabase.py` script processes your documents into smaller chunks and stores them in Chroma for fast retrieval.
- **Query Handling**: When you ask a question, the chatbot retrieves the most relevant document chunks, then uses Ollama's model to generate a response.

## Troubleshooting

- **Ollama Not Running**: Ensure you've started the Ollama server (`ollama serve`).
- **Chroma Issues**: If you have problems with the Chroma database, make sure the `CHROMA_DIRECTORY` path in your `.env` file is correct.
