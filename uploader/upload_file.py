import requests, json, ssl
from decouple import config
from get_ul_url import ul_url

#Enter Path to the file
path = input("Enter Path : ")
print("Uploading...")
files = { 'file' : ("@"+path,open(path,'rb'), 'multipart/form-data')}
session = requests.Session()

login_id = config('API_USERNAME')
key_id = config('API_PASSWORD')

def ul_video(ul_url):
    headers = { "login":login_id,"key":key_id }
    try:
        response = session.post(ul_url,files = files,headers=headers)
        data = json.loads(response.text)
        url = data.get('result').get('url')
        size_in_bytes = data.get('result').get('size')
        mb = int(size_in_bytes)/1024/1024
        return url
    except Exception as e:
        print(e)

url = ul_video(ul_url)
print(url)
