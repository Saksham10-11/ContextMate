from dotenv import load_dotenv
import shutil
import os

load_dotenv()
chroma_directory = os.getenv("CHROMA_DIRECTORY")
DIR_PATH = os.getenv("DIRECTORY_PATH")

def clear_database():
    if os.path.exists(chroma_directory):
        shutil.rmtree(chroma_directory)

if __name__ == '__main__':
    clear_database()