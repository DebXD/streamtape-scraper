import requests
from rich.console import Console
from uploader.get_ul_url import *

console = Console()
#Enter Path to the file
path = input("Enter Path : ")
console.print("Uploading...", style="bold red")
files = { 'file' : ("@"+path,open(path,'rb'), 'multipart/form-data')}
session = requests.Session()

def ul_video(ul_url):
    headers = { "login":login_id,"key":key_id }
    try:
        response = session.post(ul_url,files = files,headers=headers)
        data = json.loads(response.text)
        url = data.get('result').get('url')
        #size_in_bytes = data.get('result').get('size')
        #mb = int(size_in_bytes)/1024/1024
        console.print("Uploaded Successfully", style = "bold green")
        return url
    except Exception as e:
        console.print(e)
url = ul_video(ul_url)
