import requests,json
from decouple import config
from rich.console import Console

console = Console()

login_id = config('API_USERNAME')
key = config('API_PASSWORD')

def acc_info():
    headers = {'login' : login_id, 'key' : key }
    console.print("Checking credentials..", style="italic #87ceeb" )
    
    response = requests.get('https://api.streamtape.com/account/info?',headers)
    data = json.loads(response.text)
    status_code = data.get("status")
    return status_code

status_code = acc_info()

