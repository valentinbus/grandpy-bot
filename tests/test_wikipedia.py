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

# def test_get_anecdote(monkeypatch):
#     def mock_get_wiki_title(coordinates):
#         return "Le test est ok :)"

#     class MockRequestsGet:
#         def __init__(self, url, params):
#             pass

#         def json(self):
#             return {
#                 "query": {
#                     "pages": {
#                         "115750": {
#                             "extract": "Le test est ok :)"
#                         }
#                     } 
#                 }
#             }

#     monkeypatch.setattr("requests.get", MockRequestsGet)
#     monkeypatch.setattr("Wikipedia._get_wiki_title", mock_get_wiki_title)

#     assert wk.get_anecdote({"lat":48.85, "lng":2.29}) == "Le test est ok :)"