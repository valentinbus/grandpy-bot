import os
import requests


BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
GMAPS_API_KEY1 = os.getenv("GMAPS_API_KEY1")
GMAPS_API_KEY2 = os.getenv("GMAPS_API_KEY2")

SESSION = requests.session()

class Gmaps:
    def find_coordinates(self, q):
        coordinates = dict()

        PARAMS = {
            "key" : GMAPS_API_KEY1,
            "address" : q
        }
        coordinates = dict()
        response = (SESSION.get(url=BASE_URL, params=PARAMS)).json()
        
        if response["status"] == "ZERO_RESULTS":
            return None
        else:
            for elem in response["results"]:
                return elem["geometry"]["location"]

    def url_embed(self, coordinates):
        return f"https://www.google.com/maps/embed/v1/place?key={GMAPS_API_KEY2}&q=null&center={coordinates['lat']},{coordinates['lng']}"

    def default_url(self):
        return f"https://www.google.com/maps/embed/v1/place?key={GMAPS_API_KEY2}&q=cassis"
