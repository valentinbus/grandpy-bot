import os
import requests


BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
GMAPS_API_KEY1 = os.getenv("GMAPS_API_KEY1")
GMAPS_API_KEY2 = os.getenv("GMAPS_API_KEY2")


class Gmaps:
    """
    Using to find location and give good url to display the good place
    """
    def find_coordinates(self, q):
        """
        Take the user input and return the location's coordinate
        """
        coordinates = dict()

        PARAMS = {
            "key": GMAPS_API_KEY1,
            "address": q
        }
        coordinates = dict()
        response = (requests.get(url=BASE_URL, params=PARAMS)).json()

        if response["status"] == "ZERO_RESULTS":
            return None
        else:
            for elem in response["results"]:
                return elem["geometry"]["location"]

    def url_embed(self, coordinates):
        """
        Take location's coordinate and return the url to display
        good location on map
        """
        return (
            f"https://www.google.com/maps/embed/v1/place"
            f"?key={GMAPS_API_KEY2}&q=null&center={coordinates['lat']},"
            f"{coordinates['lng']}"
        )

    def default_url(self):
        """
        Set defaut display map on chatbot interface
        """
        return (
            "https://www.google.com/maps/embed/v1/place?"
            f"key={GMAPS_API_KEY2}&q=cassis"
        )
