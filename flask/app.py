from flask import (
    Flask,
    request,
    render_template,
    jsonify,
    Response,
    make_response
)
from backend.wikipedia import Wikipedia
from backend.gmaps import Gmaps
from backend.parser import Parser
from flask_cors import CORS, cross_origin

import json


wk = Wikipedia()
gmaps = Gmaps()
parser = Parser()

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET"])
def index():
    googleurl = gmaps.default_url()
    return render_template("bot.html", googleurl=googleurl)


@app.route('/process', methods=["POST"])
def response():
    if request.method == "POST":

        query = request.form['query']
        if query.lower().startswith("bonjour"):
            coordinates = None
            google_url = gmaps.default_url()
            data = (
                "Bonjour mon enfant, demande moi où "
                "se situe un endroit et je t'indiquerai "
                "son emplacement sur la carte \U0001F50D\n"
                "Je ferai également en sorte de trouver une anecdote "
                "si ma mémoire ne me fait pas défaut \U0001F62C"
            )

        else:
            q = parser.parser(query)
            coordinates = gmaps.find_coordinates(query)

            if coordinates:
                google_url = gmaps.url_embed(coordinates)
                data = wk.get_anecdote(coordinates)
            else:
                google_url = gmaps.default_url()
                data = (
                    "Désolé GrandPy a du mal à entendre ... "
                    "Peux-tu reformuler ta question ? "
                    "Peut être que ça me rappelera quelque chose..."
                )

        response = {
            "google_url": google_url,
            "coordinates": coordinates,
            "data": data
        }

        return jsonify(response)
    return jsonify({"error": "no response"})


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=80,
    )
