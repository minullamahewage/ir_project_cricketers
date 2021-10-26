from elasticsearch import Elasticsearch, helpers
import json
import re

es = Elasticsearch([{'host': '127.0.0.1', 'port':9200}])

def search(query):
    print(query)
    results = es.search(index='index-cricketers', body={
        "size": 10,
        "query": {
            "multi_match": {
                "query": query,
                "type": "best_fields",
                "fields": [
                    "Full_Name", "Full_Name_si", "Born", "Education","Matches","Runs","Average","Half-centuries",
                    "Centuries","Wickets","Economy","Player_Bio"]

            }
        },
    })

    return post_processing(results)

def post_processing(results):
    cricketers = []
    for i in range(len(results['hits']['hits'])):
        cricketers.append(results['hits']['hits'][i]['_source'])

    return cricketers

# if __name__ == "__main__":
#     print(search("පිතිකරු"))

# fields = ["id","Full Name","Born","Age","Batting Style","Bowling Style","Playing Role","Education","Matches","Runs","Average","Half-centuries",
# "Centuries","Wickets","Economy","Player Bio","Full Name si"]