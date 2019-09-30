import pytest
import requests
import os
from flask.backend.gmaps import (
    Gmaps, GMAPS_API_KEY1, GMAPS_API_KEY2, BASE_URL
)

gmaps = Gmaps()

def test_find_coordinates(monkeypatch):
    class MockRequestsGet:
        def __init__(self, url, params):
            pass

        def json(self):
            return {
                "results": [
                    {
                        "geometry": {
                            "location": {
                                "lat": 48.85,
                                "lng": 2.29
                            }
                        }
                    }
                ],
                "status": "OK"
            }


    monkeypatch.setattr("requests.get", MockRequestsGet)
    assert gmaps.find_coordinates("ou est paris") == {"lat":48.85, "lng":2.29}

def test_find_coordinates(monkeypatch):
    class MockRequestsGet:
        def __init__(self, url, params):
            pass

        def json(self):
            return {
                "results": [
                    {
                        "geometry": {
                            "location": {
                                "lat": 48.85,
                                "lng": 2.29
                            }
                        }
                    }
                ],
                "status": "ZERO_RESULTS"
            }
    monkeypatch.setattr("requests.get", MockRequestsGet)
    assert gmaps.find_coordinates("idnzifnef") == None


def test_url_embed(monkeypatch):
    assert gmaps.url_embed({"lat":48.85, "lng":2.29}) == (
            f"https://www.google.com/maps/embed/v1/place"
            f"?key={GMAPS_API_KEY2}&q=null&center=48.85,"
            f"2.29"
        )
