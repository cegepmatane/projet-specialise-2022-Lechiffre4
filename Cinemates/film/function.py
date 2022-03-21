from imdb import Cinemagoer
import os
from bs4 import BeautifulSoup
import requests

ia = Cinemagoer()

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


ia = Cinemagoer()

def url_clean(url):
    base, ext = os.path.splitext(url)
    i = url.count('@')
    s2 = url.split('@')[0]
    url = s2 + '@' * i + ext
    return url



def getComment(film_id):
    bestComment = []
    url = "https://www.imdb.com/title/tt"+str(film_id)+"/?ref_=fn_al_tt_1"
    req = requests.get(url, headers)
    doc = BeautifulSoup(req.content,"html.parser")
    parent = doc.find("body").find("div",{"class":"styles__MetaDataContainer-sc-12uhu9s-0 cgqHBf"}).find_all("div",{"class":"ipc-html-content ipc-html-content--base"})

    for i in parent:
        bestComment.append(i.getText())

    bestComment = bestComment[0]
    return bestComment

def GetInfo(id):
    
        film = ia.get_movie(id)

        #Title
        try:
            title = film["title"]
        except KeyError as e:
            print(e)
            title = "No title found"

        #Image
        try:
            image = film['cover']
            image = url_clean(image)
        except KeyError as e:
            print(e)
            image = "https://thumbs.dreamstime.com/b/aucune-photo-ou-ic%C3%B4ne-d-image-vide-chargement-images-marque-manquante-non-disponible-%C3%A0-venir-silhouette-nature-simple-dans-l-215973362.jpg"

        #directors
        try:
            raw_authors = film["director"]
            authors = []
            authors_str = ""
            for author in raw_authors:
                authors.append(author["name"])
            
            for i in authors:
                authors_str += i
                if (i != authors[len(authors)-1]):
                    authors_str += " / "

        except KeyError as e:
            print(e)
            authors_str = "No directors found"

        #Writer
        try:
            raw_writers = film["writer"]
            writers = []
            writers_str = ""
            for writer in raw_writers:
                writers.append(writer["name"])

            for i in writers:
                writers_str += i
                if (i != writers[len(writers)-1]):
                    writers_str += " / "

        except KeyError as e:
            print(e)
            writers_str = "No writers found"

        #cast
        try:
            raw_cast = film["cast"]
            actors = []
            actors_str = ""
            for actor in raw_cast:
                actors.append(actor["name"])

            actors = actors[:5]
            for i in actors:
                actors_str += i
                if (i != actors[len(actors)-1]):
                    actors_str += " / "

        except KeyError as e:
            print(e)
            actors_str = "No actors found"

        #rating
        try:
            rate = film["rating"]
        except KeyError as e:
            print(e)
            rate = "No rating found"

        #Genre
        try:
            genre = film["genres"]
            genre_str = ""
            for i in genre:
                genre_str += i
                if (i != genre[len(genre)-1]):
                    genre_str += " / "
                    
        except KeyError as e:
            print(e)
            genre_str = "No categories found"

        #Plot
        try:
            plot = film["plot"]
            plot_str = ""
            for i in plot:
                plot_str += i
        except KeyError as e:
            print(e)
            plot_str = "No synopsis found"

        try : 
            bestComment = getComment(str(id))
        except :
            bestComment = "No comments found"


        #classify information in a dict
        infos = {
            "title": title,
            "image": image,
            "author": authors_str,
            "rate": rate,
            "genre": genre_str,
            "writer": writers_str,
            "cast": actors_str,
            "plot": plot_str,
            "comment": bestComment
        }
        return infos
