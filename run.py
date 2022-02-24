from rich.console import Console
from account_info import status_code

console = Console()

if status_code == 403:
    console.print("Please set your credentials correctly before runnning the project.", style = "bold red")
else:
    dlorul = input("Do you want to download or upload(dl/ul) : ")
    
    if dlorul == "dl":
        #Download
        from downloader.get_dl_url import download_link
        from downloader.dl import *

        download(download_link)


    elif dlorul == "ul":
        #Upload

        from uploader.upload_file import *

        console.print(f"Here is your URL : {url}", style="bold #00FFFF")

    else:
        console.print("You have entered wrong input;\nGoodBye",style="italic red")
