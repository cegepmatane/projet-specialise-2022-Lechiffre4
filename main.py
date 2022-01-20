from bs4 import BeautifulSoup
import requests

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


def ProcessName(film_name):
    film_name = film_name.lower()
    film_name = film_name.replace(":","")
    film_name = film_name.replace("-"," ")
    film_name = film_name.replace(" ","_")
    return film_name
    




film_name = input("entrez le nom d'un film : ")
film_name = ProcessName(film_name)
url = "https://www.rottentomatoes.com/m/"+ film_name
req = requests.get(url, headers)
doc = BeautifulSoup(req.content,"html.parser")
print("".join(doc.find("h1").strings))

#print(doc.prettify())


