import pytest
import os
from backend.gmaps import Gmaps, GMAPS_API_KEY, BASE_URL

gmaps = Gmaps()

def test_find_coordinates():
    assert gmaps.find_coordinates("tour eiffel") == {"lat": 48.85837009999999, "lng": 2.2944813}
    assert gmaps.find_coordinates("cassis") == {"lat": 43.215134, "lng": 5.53712}

def test_url_embed():
    coordinates = {"lat": 48.85837009999999, "lng": 2.2944813}
    assert gmaps.url_embed(coordinates) == f"https://www.google.com/maps/embed/v1/place?key={GMAPS_API_KEY}&q=null&center=48.85837009999999,2.2944813"

    coordinates = {"lat": 43.215134, "lng": 5.53712}
    assert gmaps.url_embed(coordinates) == f"https://www.google.com/maps/embed/v1/place?key={GMAPS_API_KEY}&q=null&center=43.215134,5.53712"

