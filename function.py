from bs4 import BeautifulSoup
import requests
from deep_translator import GoogleTranslator

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

def listfilmIMBD(film_name):
    IMBDList = []
    url = "https://www.imdb.com/find?q="+film_name+"&s=tt&ttype=ft&ref_=fn_ft"
    req = requests.get(url, headers)
    doc = BeautifulSoup(req.content,"html.parser")
    parent = doc.find("body").find("table").find_all("td",{"class":"result_text"})

    for i in parent:
        IMBDList.append(i.find("a").getText())

    #print(IMBDList)
    return IMBDList

def listfilmAllocine(film_name):
    AllocineList = []
    url = "https://www.allocine.fr/rechercher/movie/?q="+film_name
    req = requests.get(url, headers)
    doc = BeautifulSoup(req.content,"html.parser")
    parent = doc.find("body").find_all("h2")
    for i in parent:
        title = i.getText()
        title = title.replace("\n","")
        title_translated = GoogleTranslator(source='auto',target='en').translate(title)
        AllocineList.append(title_translated)
    #print(AllocineList)
    return AllocineList