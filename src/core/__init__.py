import os

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOTENV_PATH = os.path.join(BASE_DIR, '..', '.env')
load_dotenv(dotenv_path=os.path.abspath(DOTENV_PATH))