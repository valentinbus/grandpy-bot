from flask import Flask, request, render_template, jsonify, Response, make_response
from backend.wikipedia.wikipedia import Wikipedia
from flask_cors import CORS, cross_origin

import json 

from pprint import pprint

wk = Wikipedia()

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET", "POST"])
def index():
    data=None
    if request.method == "POST":
        query = request.form['query']
        data = wk.get_all_wiki_info(query)
        
        pprint(f"DATA====>{data}")
        print(f"QUERY====>{query}")
    return render_template('bot.html', data=data)


@app.route('/test', methods=["GET", "POST"])
def response():
    if request.method=='POST':
        data = request.form['test']
        print(data)
    return render_template("test.html")


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0', 
        port=80,
    )
