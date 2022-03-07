from imdb import Cinemagoer

ia = Cinemagoer()

def GetInfo(id):
    title = ia.get_movie(id)
    title = title["title"]
    return title
