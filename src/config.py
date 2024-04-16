import os

from dotenv import load_dotenv

from utils.utils import to_json


dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path)

FILE_PATH = os.environ.get("FILE_PATH")
JSON_FILE_PATH = os.environ.get("JSON_FILE_PATH")

JSON_DATA = to_json(FILE_PATH, JSON_FILE_PATH)
