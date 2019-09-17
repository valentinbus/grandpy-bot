import requests


BASE_URL = "https://fr.wikipedia.org/w/api.php"
SESSION = requests.session()


def get_all_wiki_info(search):
    """
    Get info from wikipedia
    """

    params = {
        "action" : "opensearch",
        "search" : search, 
        "format" : "json"
        }

    r = SESSION.get(url=BASE_URL, params=params)
    data = r.json()
    return data
 
def test(param):
    return param