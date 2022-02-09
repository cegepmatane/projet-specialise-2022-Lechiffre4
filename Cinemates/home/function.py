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

    films_dict = dict(list(enumerate(IMBDList)))
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
    urls = ["https://www.imdb.com/title/tt0082971/?ref_=fn_al_tt_2", "https://www.senscritique.com/film/Les_Aventuriers_de_l_arche_perdue/439783"]
    req1 = requests.get(urls[0], headers)
    req2 = requests.get(urls[1], headers)
    doc1 = BeautifulSoup(req1.content,"html.parser")
    doc2 = BeautifulSoup(req2.content,"html.parser")

    """Scrap Genre"""

    genresIMDb = doc1.find("body").find_all("a",{"class":"GenresAndPlot__GenreChip-sc-cum89p-3 LKJMs ipc-chip ipc-chip--on-baseAlt"})
    for i in range(0,len(genresIMDb)):
        genresIMDb[i] = genresIMDb[i].getText().lower()
        genresIMDb[i] = GoogleTranslator(source='auto',target='en').translate(genresIMDb[i])
    
    genresSens = doc2.find("body").find_all("span",{"itemprop":"genre"})
    for i in range (0, len(genresSens)):
        genresSens[i] = genresSens[i].getText().lower()
        genresSens[i] = GoogleTranslator(source='auto',target='en').translate(genresSens[i])


    genres = list(set().union(genresSens, genresIMDb))

    

    """Scrap note"""
    notesIMDb = doc1.find("body").find_all("span",{"class":"AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV"})
    notesIMDb = notesIMDb[0].getText()


    notesSens = doc2.find("body").find_all("span",{"itemprop":"ratingValue"})
    notesSens = notesSens[0].getText()

    notes = [float(notesIMDb), float(notesSens)]
    moyenneG = sum(notes)/len(notes)

    
    return genres, notes, moyenneG






def SortFilmOutput(usersearch, listfilms):
    filmlistdisplayed = []
    usersearch = usersearch.lower()
    for i in listfilms:
        lowerI = i.lower()
        if (lowerI.find(usersearch) != -1):
            filmlistdisplayed.append(i)
        
    return filmlistdisplayed


