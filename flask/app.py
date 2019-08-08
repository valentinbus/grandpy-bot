from flask import Flask, request, render_template, jsonify, Response
from backend import wikipedia



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('bot.html')


@app.route('/wiki_response', methods=["GET", "POST"])
def response():
    #q = resquests.get('')
    return jsonify(wikipedia.get_all_wiki_info('cassis')
)
if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0', 
        port=80
    )
