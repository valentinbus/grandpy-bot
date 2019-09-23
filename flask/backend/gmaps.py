import os
import requests


BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
GMAPS_API_KEY = os.getenv("GMAPS_API_KEY")

SESSION = requests.session()

class Gmaps:
    def find_coordinates(self, q):
        coordinates = dict()

        PARAMS = {
            "key" : GMAPS_API_KEY,
            "address" : q
        }
        coordinates = dict()
        response = (SESSION.get(url=BASE_URL, params=PARAMS)).json()

        for elem in response["results"]:
            return elem["geometry"]["location"]
        return "GrandPy a peut être mal entendu mais rien ne me rappel ce que tu viens de dire..."
