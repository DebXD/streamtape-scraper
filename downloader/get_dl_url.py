import requests ,json, time
from rich.console import Console
from decouple import config
from downloader.get_file_id import file_id

console = Console()
console.print("Processing...", style="bold cyan")

login_key = config('API_USERNAME')
key = config('API_PASSWORD')

def get_ticket(file_id):
    headers = {'file':file_id,'login':login_key,'key':key}
    response = requests.get("https://api.strtape.tech/file/dlticket?",headers)
    data = json.loads(response.text)

    ticket = data.get('result').get('ticket')
    return ticket
    
ticket = get_ticket(file_id)

for i in range(3,0,-1):
        console.print(f"Please wait for {i} sec...", style="bold #FFFF00")
        time.sleep(1)
        #without this sleep method api will return  error 403[forbidden]

def dl_url(ticket,file_id):
    headers = {'file':file_id,'ticket':ticket,'login':login_key,'key': key}
    response = requests.get("https://api.strtape.tech/file/dl?",headers)
    data = json.loads(response.text)
    link = data.get('result').get('url')
    byte_size = data.get('result').get('size')
    size_in_MB = int(byte_size/1024/1024)
    console.print(f'File Size : {size_in_MB}MB', style = "bold red")
    return link
download_link = dl_url(ticket,file_id)
    
