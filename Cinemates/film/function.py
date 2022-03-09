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
            authors_str = ""
            for author in raw_authors:
                authors.append(author["name"])
            
            for str in authors:
                authors_str += str
                if (str != authors[len(authors)-1]):
                    authors_str += " / "

        except KeyError as e:
            print(e)
            authors_str = "null"

        #Writer
        try:
            raw_writers = film["writer"]
            writers = []
            writers_str = ""
            for writer in raw_writers:
                writers.append(writer["name"])

            for str in writers:
                writers_str += str
                if (str != writers[len(writers)-1]):
                    writers_str += " / "

        except KeyError as e:
            print(e)
            writers_str = "null"

        #cast
        try:
            raw_cast = film["cast"]
            actors = []
            actors_str = ""
            for actor in raw_cast:
                actors.append(actor["name"])

            actors = actors[:5]
            for str in actors:
                actors_str += str
                if (str != actors[len(actors)-1]):
                    actors_str += " / "

        except KeyError as e:
            print(e)
            actors_str = "null"

        #rating
        try:
            rate = film["rating"]
        except KeyError as e:
            print(e)
            rate = "null"

        #Genre
        try:
            genre = film["genres"]
            genre_str = ""
            for str in genre:
                genre_str += str
                if (str != genre[len(genre)-1]):
                    genre_str += " / "
                    
        except KeyError as e:
            print(e)
            genre_str = "null"

        #Plot
        try:
            plot = film["plot"]
            plot_str = ""
            for str in plot:
                plot_str += str
        except KeyError as e:
            print(e)
            plot_str = "null"

        #classify information in a dict
        infos = {
            "title": title,
            "image": image,
            "author": authors_str,
            "rate": rate,
            "genre": genre_str,
            "writer": writers_str,
            "cast": actors_str,
            "plot": plot_str
        }
        return infos

#GetInfo(6263850)   



