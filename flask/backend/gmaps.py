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
        return response

    def url_embed(self, coordinates):
        return f"https://www.google.com/maps/embed/v1/place?key={GMAPS_API_KEY}&q=null&center={coordinates['lat']},{coordinates['lng']}"

    def default_url(self):
        return f"https://www.google.com/maps/embed/v1/place?key={GMAPS_API_KEY}&q=cassis"