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

def InfoFilm():
    listInfo = []
    urls = ["https://www.imdb.com/title/tt0082971/?ref_=fn_al_tt_2", "https://www.allocine.fr/film/fichefilm_gen_cfilm=121.html"]
    req1 = requests.get(urls[0], headers)
    req2 = requests.get(urls[1], headers)
    doc1 = BeautifulSoup(req1.content,"html.parser")
    doc2 = BeautifulSoup(req2.content,"html.parser")

    """Scrap Genre"""
    genres = doc1.find("body").find_all("a",{"class":"GenresAndPlot__GenreChip-sc-cum89p-3 LKJMs ipc-chip ipc-chip--on-baseAlt"})
    for i in range(0,len(genres)):
        genres[i] = genres[i].getText()
    
    """Scrap note"""
    notesIMDb = doc1.find("body").find_all("span",{"class":"AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV"})
    notesIMDb = notesIMDb[0].getText()
    notesAllociné = doc2.find("body").find_all("span",{"class":"AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV"})
    notesIMDb = notesIMDb[0].getText()

    return notesIMDb

