import pytest
import requests
import os
from flask.backend.gmaps import Gmaps, GMAPS_API_KEY1, GMAPS_API_KEY2, BASE_URL

gmaps = Gmaps()

def test_find_coordinates(monkeypatch):

    def mock_request(query):
        class Mock_Session:
            def get(self, url, params):
                return Mock_Get()

        class Mock_Get:
            def json(self):
                return {
                    "results" : [
                        {
                            "geometry": {
                                "location" : {
                                    "lat" : 48.85,
                                    "lng" : 2.29
                                }
                            }
                        }
                    ]
                }


    monkeypatch.setattr("session.get", mock_request)
    assert gmaps.find_coordinates("ou est paris") == {"lat":48.85, "lng":2.29}
