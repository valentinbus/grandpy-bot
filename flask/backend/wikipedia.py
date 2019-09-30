import requests
import re
import json


BASE_URL = "https://fr.wikipedia.org/w/api.php"


class Wikipedia:
    """
    Use to got anecdote used in grandpybot's response
    """
    def _get_wiki_title(self, coordinates):
        """
        To match gmaps informations and wikipedia's information we give
        coordinates find by geocode (gmaps) to geosearch function
        (provides by wikipedia) and return Title of an article
        """

        formated_coord = f"{coordinates['lat']}|{coordinates['lng']}"

        PARAMS = {
            "action": "query",
            "list": "geosearch",
            "format": "json",
            "gsradius": 1000,
            "gscoord": formated_coord
        }

        return requests.get(
            url=BASE_URL, params=PARAMS
        ).json()['query']['geosearch'][0]['title']

    def get_anecdote(self, coordinates):
        """
        With title provides by _get_wiki_title() method we can extract an
        anectode from wikipedia, uses in grandpybot response
        """
        title = self._get_wiki_title(coordinates)
        PARAMS = {
            "action": "query",
            "prop": "extracts",
            "exchars": 175,
            "titles": title,
            "format": "json",
            "explaintext": True
        }

        response = requests.get(url=BASE_URL, params=PARAMS).json()
        nb_page = [elem for elem in response["query"]["pages"]]

        return (
            'Oh oui je vois ...\nCela me rappel que '
            f'{response["query"]["pages"][nb_page[0]]["extract"]}'
        )
