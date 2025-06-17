import threading
import requests
from bs4 import BeautifulSoup

urls=[
    'https://python.langchain.com/docs/introduction/',
    'https://python.langchain.com/docs/tutorials/',
    'https://python.langchain.com/docs/how_to/'
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    #print(f" {soup.text} in this {url}")
    print(f"Fetched {len(soup.text)} in this {url}")

threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("ALL web page fetched")        
