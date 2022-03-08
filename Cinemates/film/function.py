from imdb import Cinemagoer
import os

ia = Cinemagoer()

def url_clean(url):
    base, ext = os.path.splitext(url)
    i = url.count('@')
    s2 = url.split('@')[0]
    url = s2 + '@' * i + ext
    return url


def GetInfo(id):
    
        film = ia.get_movie(id)

        #Title
        try:
            title = film["title"]
        except KeyError as e:
            print(e)
            title = "null"

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
            for author in raw_authors:
                authors.append(author["name"])
        except KeyError as e:
            print(e)
            authors = ["null"]

        #Writer
        try:
            raw_writers = film["writer"]
            writers = []
            for writer in raw_writers:
                writers.append(writer["name"])
        except KeyError as e:
            print(e)
            writers = ["null"]

        #cast
        try:
            raw_cast = film["cast"]
            actors = []
            for actor in raw_cast:
                actors.append(actor["name"])
        except KeyError as e:
            print(e)
            actors = ["null"]

        #rating
        try:
            rate = film["rating"]
        except KeyError as e:
            print(e)
            rate = "null"

        #Genre
        try:
            genre = film["genres"]
        except KeyError as e:
            print(e)
            gene = "null"

        #Plot
        try:
            plot = film["plot"]
        except KeyError as e:
            print(e)
            plot = "null"

        #classify information in a dict
        infos = {
            "title": title,
            "image": image,
            "author": authors,
            "rate": rate,
            "genre": genre,
            "writer": writers,
            "cast": actors,
            "plot": plot
        }
        return infos

GetInfo(6263850)   



