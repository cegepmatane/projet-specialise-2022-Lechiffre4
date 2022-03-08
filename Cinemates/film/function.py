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
    title = film["title"]

    #Image
    image = film['cover']
    image = url_clean(image)

    #directors
    raw_authors = film["director"]
    authors = []
    for author in raw_authors:
        authors.append(author["name"])

    #Writer
    raw_writers = film["writer"]
    writers = []
    for writer in raw_writers:
        writers.append(writer["name"])

    #cast
    raw_cast = film["cast"]
    actors = []
    for actor in raw_cast:
        actors.append(actor["name"])

    #rating
    rate = film["rating"]

    #Genre
    genre = film["genres"]

    #Plot
    plot = film["plot"]

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
        



