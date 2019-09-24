import requests
import re
import json


BASE_URL = "https://fr.wikipedia.org/w/api.php"
SESSION = requests.session()


class Wikipedia:      

    def _get_wiki_title(self, coordinates):
        formated_coord = f"{coordinates['lat']}|{coordinates['lng']}"
        
        PARAMS = {
            "action" : "query",
            "list" : "geosearch",
            "format" : "json",
            "gsradius" : 1000,
            "gscoord": formated_coord
        }

        return SESSION.get(url=BASE_URL, params=PARAMS).json()['query']['geosearch'][0]['title']

    def get_anecdote(self, coordinates):
        title = self._get_wiki_title(coordinates)
        PARAMS = {
            "action" : "query", 
            "prop" : "extracts",
            "exchars" : 175,
            "titles" : title,
            "format" : "json",
            "explaintext" : True
        }

        response = SESSION.get(url=BASE_URL, params=PARAMS).json()
        nb_page = [elem for elem in response["query"]["pages"]]

        return f'Oh oui je vois ...\nCela me rappel que {response["query"]["pages"][nb_page[0]]["extract"]}'
