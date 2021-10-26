from flask import Flask
import pickle
from flask import jsonify, request
from elasticsearch import Elasticsearch, helpers
import requests
from flask import flash, render_template, request, redirect, jsonify

es = Elasticsearch([{'host': '127.0.0.1', 'port':9200}])
from search import search
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def search_actor():
    if request.method == 'POST':
        if request.form['query']:
            query = request.form['query']
            # print(query)
        else:
            query = ''
        results = search(query)


    # keyword = request.form['keyword']

    # query_body = {
    #     "query": {
    #         "match": {
    #             "name_si": keyword
    #         }
    #     }
    # }
    #
    # res = es.search(index="index-actors", body=query_body)
        return jsonify(results)
        # return render_template('index.html', actors= actors, names = names, real_names = real_names, birthdays = birthdays, diedes = diedes, addresses = addresses)
    else:
        return {"task": "profit!"}
        # return render_template('index.html', actors= '', names = '', real_names = '', birthdays = '', diedes = '', addresses = '')


if __name__ == '__main__':
    app.run()
