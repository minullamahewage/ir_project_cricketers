from flask import Flask
from flask import jsonify, request
from elasticsearch import Elasticsearch
from flask import flash, render_template, request, redirect, jsonify

es = Elasticsearch([{'host': '127.0.0.1', 'port':9200}])
from search import search
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def search_actor():
    if request.method == 'POST':
        if request.form['search_query']:
            query = request.form['search_query']
            print(query)
        else:
            query = ''
        cricketers = search(query)

        return render_template('index.html', cricketers= cricketers)
    else:
        return render_template('index.html', cricketers='')


if __name__ == '__main__':
    app.run(debug=True)
