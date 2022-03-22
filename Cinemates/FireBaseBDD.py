import pyrebase
from decouple import config


firebaseConfig = {
  "apiKey": config("apiKey"),
  "authDomain": config("authDomain"),
  "databaseURL": config("databaseURL"),
  "projectId": config("projectId"),
  "storageBucket": config("storageBucket"),
  "messagingSenderId": config("messagingSenderId"),
  "appId": config("appId"),
  "measurementId": config("measurementId")
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

#Test Push data 
def addFilm(jsonFilmInfo):
    db.child("Films").push(jsonFilmInfo)
    print("Film added")

def searchFilm(film_id):
    films = db.child("Films").get()
    print(films.val())
    if films.val() != None:
        for film in films.each():
            if film.val()["id"] == film_id :
                return film
    else :
        return None


def addResearch(user_research, filmsName, filmsID, filmsPics):
    research = user_research.lower()
    for i in range (0,len(filmsName)):
        data = {
            "name": filmsName[i],
            "film_id": filmsID[i],
            "film_pic": filmsPics[i]
        }
        db.child("Research").child(research).push(data)

def searchResearch(user_research):
    research = user_research.lower()
    research = db.child("Research").child(research).get()
    if research.val() == None:
        print("this research doesn't exist")
        return None
    else:
        films_names = []
        films_links = []
        films_pics = []
        for film in research.each():
            films_names.append(film.val()["name"])
            films_links.append(film.val()["film_id"])
            films_pics.append(film.val()["film_pic"])
        return films_names,films_links,films_pics



print(searchResearch("deadpool")[0])