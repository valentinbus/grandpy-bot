from flask import Flask, request, render_template, jsonify, Response
from backend.wikipedia import wikipedia
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return render_template('bot.html')


@app.route('/wiki_response', methods=["GET"])
def response():

    query = " ".join([arg for arg in request.args])

    if query != "":
        return jsonify(wikipedia.get_all_wiki_info(query))
    else:
        return jsonify(wikipedia.get_all_wiki_info(query).get("error").get("info"))


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0', 
        port=80,
    )
