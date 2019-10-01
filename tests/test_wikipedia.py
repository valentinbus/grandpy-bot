import pytest
import requests
from flask.backend.wikipedia import (
    Wikipedia, BASE_URL
)

wk = Wikipedia()


def test_get_wiki_title(monkeypatch):
    class MockRequestsGet:
        def __init__(self, url, params):
            pass

        def json(self):
            return {
                "query": {
                    "geosearch": [
                        {
                            "title": "Le test est ok"
                        }
                    ]
                }
            }

    coordinates = {"lat": 37.786971, "lng": -122.399677}
    monkeypatch.setattr("requests.get", MockRequestsGet)
    assert wk._get_wiki_title(coordinates) == "Le test est ok"

def test_get_anectode(monkeypatch):
    coordinates = {"lat": 37.786971, "lng": -122.399677}
    
    def mock_get_title(self, coordinates):
        return "TITLE"

    class MockRequestsGet:
        def __init__(self, url, params):
            pass

        def json(self):
            return {
                "query": {
                    "pages": {
                        "11": {
                            "extract": "Le test est OK :)"
                        }
                    }
                }
            }

    monkeypatch.setattr(Wikipedia, "_get_wiki_title", mock_get_title)
    monkeypatch.setattr("requests.get", MockRequestsGet)

    assert wk.get_anecdote(coordinates) == (
            'Oh oui je vois ...\nCela me rappel que '
            'Le test est OK :)'
        )
