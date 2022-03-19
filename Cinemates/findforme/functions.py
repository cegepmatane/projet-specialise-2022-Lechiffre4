from imdb import Cinemagoer
import random
import os


ia = Cinemagoer()

def url_clean(url):
    base, ext = os.path.splitext(url)
    i = url.count('@')
    s2 = url.split('@')[0]
    url = s2 + '@' * i + ext
    return url


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

def getRandomFilm(category):
    list_films = []
    films = ia.search_keyword(category);
    films = ia.get_keyword(films[random.randint(0,len(films))]);


    for i in range(0,3):
        result = None


        while result is None :
            try :
                random_index = random.randint(0,len(films))
                film = films[random_index]['title']

                list_films.append(film)
                result = 0
            except:
                pass
    

    for film in list_films:
        if list_films.count(film) > 1:
            getRandomFilm()

    return list_films;


def getfilmID(film_name):
    film_id = ia.search_movie(film_name)
    film_id = film_id[0].movieID
    return film_id;
