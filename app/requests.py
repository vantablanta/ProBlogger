import os 
from dotenv import load_dotenv
import requests
load_dotenv()

BASE_URL= os.getenv('BASE_URL')

def get_quotes():
    response = requests.get(BASE_URL).json()
    return response
