import requests, json
from decouple import config

login_id = config('API_USERNAME')
key_id = config('API_PASSWORD')
session = requests.Session()

def get_url():
    cred = { "login":login_id,"key":key_id }
    print("Please be Patient")
    response = session.get("https://api.streamtape.com/file/ul?",headers=cred,)
    
    data = json.loads(response.text)
    ul_url = data.get('result').get('url')
    return ul_url

ul_url = get_url()
    


