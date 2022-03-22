from bs4 import BeautifulSoup
import requests
from deep_translator import GoogleTranslator
from imdb import Cinemagoer
import os
import FireBaseBDD

ia = Cinemagoer()

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

def url_clean(url):
    base, ext = os.path.splitext(url)
    i = url.count('@')
    s2 = url.split('@')[0]
    url = s2 + '@' * i + ext
    return url

def getlistfilmIMBD(film_name):
    IMBDList = []
    url = "https://www.imdb.com/find?q="+film_name+"&s=tt&ttype=ft&ref_=fn_ft"
    req = requests.get(url, headers)
    doc = BeautifulSoup(req.content,"html.parser")
    parent = doc.find("body").find("table").find_all("td",{"class":"result_text"})

    for i in parent:
        IMBDList.append(i.find("a").getText())

    return IMBDList


def getfilmID(film_name):
    film_id = ia.search_movie(film_name)
    film_id = film_id[0].movieID
    return film_id;

def getPic(film_id):
    #Image
    film = ia.get_movie(film_id)
    try:
        image = film['cover']
        image = url_clean(image)
        return image
    except KeyError as e:
        image = "https://thumbs.dreamstime.com/b/aucune-photo-ou-ic%C3%B4ne-d-image-vide-chargement-images-marque-manquante-non-disponible-%C3%A0-venir-silhouette-nature-simple-dans-l-215973362.jpg"
        return image

def getlistfilmAllocine(film_name):
    AllocineList = []
    url = "https://www.allocine.fr/rechercher/movie/?q="+film_name
    print(url)
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


def sortFilmOutput(usersearch, listfilms):
    filmlistdisplayed = []
    usersearch = usersearch.lower()
    for i in listfilms:
        lowerI = i.lower()
        if (lowerI.find(usersearch) != -1):
            filmlistdisplayed.append(i)
        
    return filmlistdisplayed


