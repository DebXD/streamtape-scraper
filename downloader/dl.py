import requests, json
from rich.console import Console
from downloader.get_dl_url import *

session = requests.Session()
console = Console()

def download(download_link):
    dl_now = input("Do You want to download now! y/n : ")
    if dl_now =='y':
        console.print("Downloading🙂...Please Wait...", style = "bold blue")
        r = requests.get(download_link)
        open(file_id +'.mp4', 'wb').write(r.content)
        console.print("Download is Completed\n Exiting...", style = "italic #FFC0CB")
    else:
        console.print("OK Bye!", style = "italic violet" )