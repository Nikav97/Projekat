import requests
import json
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path=".env")
API_KEY=os.getenv("API_KEY")
kanal="UC3227n8FAEry_iEl0GKqrRQ"
url = f"https://youtube.googleapis.com/youtube/v3/channels?part=snippet%2CcontentDetails%2Cstatistics&id={kanal}&key={API_KEY}"
odgovor=requests.get(url)
print(odgovor.json())