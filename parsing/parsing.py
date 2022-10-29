import requests
from bs4 import BeautifulSoup
import json

HOST = 'https://pikabu.ru/'
url = "https://pikabu.ru/story/sbornik_tupyikh_shutok_7582749"

HEADERS={
   'accept':'',      # Не нашел где это взять)
   'user-agent':''
}

def get_html(url):
   r = requests.get(url,headers=HEADERS)

   return r
html = get_html(url)











# data = json.loads(jokes)







