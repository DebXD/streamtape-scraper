import requests ,json, time
from decouple import config

file_id = input("Enter file ID : ")
print("processing...")
#required values:
login_key = config('API_USERNAME')
key = config('API_PASSWORD')
#get this values from account panel of streamtape

def get_ticket(file_id):
    headers = {'file':file_id,'login':login_key,'key':key}
    response = requests.get("https://api.streamtape.com/file/dlticket?",headers)
    data = json.loads(response.text)

    ticket = data.get('result').get('ticket')
    return ticket
    
ticket = get_ticket(file_id)

for i in range(3,0,-1):
        print(f"Please wait for {i} sec...")
        time.sleep(1)
        #without this sleep method api will return  error 403[forbidden]

def dl_url(ticket,file_id):
    headers = {'file':file_id,'ticket':ticket,'login':'02cae24c18bff009e4a6','key':'OajOPjPlLPTZv0W'}
    response = requests.get("https://api.streamtape.com/file/dl?",headers)
    data = json.loads(response.text)
    link = data.get('result').get('url')
    byte_size = data.get('result').get('size')
    size_in_MB = int(byte_size/1024/1024)
    print(f'File Size : {size_in_MB}MB')
    return link
    
download_link = dl_url(ticket,file_id)
dl_now = input("Do You want to download now! y/n : ")

if dl_now =='y':
    print("Downloading🙂...Please Wait...")
    r = requests.get(download_link)
    open("video.mp4", 'wb').write(r.content)
    print("Download is Completed\n Exiting...")
else:
    print("OK Bye!")
    pass