import requests, json
from decouple import config
from rich.console import Console
console = Console()

login_id = config('API_USERNAME')
key_id = config('API_PASSWORD')
session = requests.Session()

def get_url():
    cred = { "login":login_id,"key":key_id }
    console.print("Please be Patient...", style = "bold yellow")
    response = session.get("https://api.strtape.tech/file/ul?",headers=cred,)
    
    data = json.loads(response.text)
    ul_url = data.get('result').get('url')
    return ul_url
ul_url = get_url()

