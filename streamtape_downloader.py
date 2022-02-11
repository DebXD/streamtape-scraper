import requests ,json, time
from rich.console import Console
from decouple import config

console = Console()
file_id = input("Enter file ID : ")
console.print("Processing...", style="bold cyan")

login_key = config('API_USERNAME')
key = config('API_PASSWORD')

def get_ticket(file_id):
    headers = {'file':file_id,'login':login_key,'key':key}
    response = requests.get("https://api.streamtape.com/file/dlticket?",headers)
    data = json.loads(response.text)

    ticket = data.get('result').get('ticket')
    return ticket
    
ticket = get_ticket(file_id)

for i in range(3,0,-1):
        console.print(f"Please wait for {i} sec...", style="bold #FFFF00")
        time.sleep(1)
        #without this sleep method api will return  error 403[forbidden]

def dl_url(ticket,file_id):
    headers = {'file':file_id,'ticket':ticket,'login':'02cae24c18bff009e4a6','key':'OajOPjPlLPTZv0W'}
    response = requests.get("https://api.streamtape.com/file/dl?",headers)
    data = json.loads(response.text)
    link = data.get('result').get('url')
    byte_size = data.get('result').get('size')
    size_in_MB = int(byte_size/1024/1024)
    console.print(f'File Size : {size_in_MB}MB', style = "bold red")
    return link
    
download_link = dl_url(ticket,file_id)
dl_now = input("Do You want to download now! y/n : ")

if dl_now =='y':
    console.print("Downloading🙂...Please Wait...", style = "bold blue")
    r = requests.get(download_link)
    open("video.mp4", 'wb').write(r.content)
    console.print("Download is Completed\n Exiting...", style = "italic #FFC0CB")
else:
    console.print("OK Bye!", style = "italic violet" )
    pass