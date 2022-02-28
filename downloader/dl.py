import requests
from rich.console import Console
from downloader.get_dl_url import *

session = requests.Session()
console = Console()

def download(download_link):
    dl_now = input("Do You want to download now! y/n : ")
   
    if dl_now =='n':
        console.print("OK Bye!", style = "italic violet" )
    else:
        console.print("Downloading🙂...Please Wait...", style = "bold blue")
        r = requests.get(download_link)
        open(file_id +'.mp4', 'wb').write(r.content)
        console.print("Download is Completed\nExiting...", style = "bold green")
        
