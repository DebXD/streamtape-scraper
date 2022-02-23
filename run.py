from rich.console import Console
console = Console()


dlorul = input("Do you want to download or upload(dl/ul) : ")

if dlorul == "dl":
    #from downloader.get_dl_url import *
    from downloader.dl import *

    download(download_link)


elif dlorul == "ul":
    #Upload
    #from uploader.get_ul_url import *
    from uploader.upload_file import *

    console.print(f"Here is your URL : {url}", style="bold #00FFFF")

else:
    console.print("You have entered wrong input;\nGoodBye",style="italic red")
