import requests
import re
import json

BASE_URL = "https://fr.wikipedia.org/w/api.php"
SESSION = requests.session()

class Wikipedia:
    def __parser(self, q):
        """
        Parse user element to being usable on wikipedia
        """

        q = q.lower()
        p = re.compile(
            "ou est \s*([^.?:;]*)$|"
            "ou se trouve\s*([^.?:;]*)$|"
            "l’adresse de\s*([^.?:;]*)$"
            "ou se situe\s*([^.?:;]*)$"
            )
        match = p.match(q)

        if match:
            result = [group for group in match.groups() if group is not None]
            return result
        
        return None


    def __get_geoloc(self, q):
        """
        Get geoloc search based on wikipedia function
        """

        PARAMS = {
            "action": "query",
            "format": "json",
            "titles": q,
            "prop": "coordinates"
        }

        data = (SESSION.get(url=BASE_URL, params=PARAMS)).json()
        pages = data['query']['pages']

        d = dict()
        for k, v in pages.items():
            d["Latitute"] = str(v['coordinates'][0]['lat'])
            d["Longitude"] = str(v['coordinates'][0]['lon'])

        return d
        

    def get_all_wiki_info(self, search):
        """
        Get info from wikipedia
        """
        search = self.__parser(search)
        params = {
            "action" : "opensearch",
            "search" : search, 
            "format" : "json"
            }

        r = SESSION.get(url=BASE_URL, params=params)

        print(f"encoding ===>{r.encoding}")
        data = r.json() 

        return data
