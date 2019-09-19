from flask import Flask, request, render_template, jsonify, Response, make_response
from backend.wikipedia.wikipedia import Wikipedia
from flask_cors import CORS, cross_origin

import json 

from pprint import pprint

wk = Wikipedia()

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET"])
def index():
    return render_template("bot.html")


@app.route('/process', methods=["POST"])
def response():
    if request.method == "POST":
        query = request.form['query']
        data = wk.get_all_wiki_info(query)
        return jsonify(data)
    return jsonify({"error":"no response"})


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0', 
        port=80,
    )
