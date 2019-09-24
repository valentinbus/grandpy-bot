from flask import Flask, request, render_template, jsonify, Response, make_response
from backend.wikipedia import Wikipedia
from backend.gmaps import Gmaps
from backend.parser import Parser
from flask_cors import CORS, cross_origin

import json 

from pprint import pprint

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
        q = parser.parser(query)
        coordinates = gmaps.find_coordinates(q)
        google_url = gmaps.url_embed(coordinates)
        data = wk.get_anecdote(coordinates)

        response = {
            "google_url":google_url,
            "coordinates":coordinates,
            "data":data
        }

        return jsonify(response)
    return jsonify({"error":"no response"})


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0', 
        port=80,
    )
