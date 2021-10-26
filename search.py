from elasticsearch import Elasticsearch, helpers
import json
import re
from fuzzywuzzy import process,fuzz

es = Elasticsearch([{'host': '127.0.0.1', 'port':9200}])

def keyword_search(query):
    # print(query)
    results = es.search(index='index-cricketers', body={
        "size": 10,
        "query": {
            "multi_match": {
                "query": query,
                "type": "best_fields",
                "fields": [
                    "Full_Name", "Full_Name_si", "Born", "Education","Player_Bio"]

            }
        },
    })
    # print(results)
    return results

def top_search(query):
    cricketers= []
    choices= [u"වැඩිම ලකුණු ලබාගත් ක්‍රීඩකයන්",u"වැඩිම කඩුලු ලබාගත් ක්‍රීඩකයන්",u"වැඩිම තරඟ ක්‍රීඩා කළ ක්‍රීඩකයන්"]
    highest = process.extractOne(u'%s' % query, choices, scorer=fuzz.ratio)
    matchIndex = choices.index(highest[0])
    value = int(re.search(r'\d+', query).group())
    if matchIndex == 0:
        results = es.search(index='index-cricketers', body=
        {
            "size": value,
            "sort" : [
                { "Runs" : "desc" }
            ]
        })
    elif matchIndex == 1:
        results = es.search(index='index-cricketers', body=
        {
            "size": value,
            "sort" : [
                { "Wickets" : "desc" }
            ]
        })
    else:
        results = es.search(index='index-cricketers', body=
        {
            "size": value,
            "sort" : [
                { "Matches" : "desc" }
            ]
        })
    return results

def post_processing(results):
    cricketers = []
    for i in range(len(results['hits']['hits'])):
        cricketers.append(results['hits']['hits'][i]['_source'])

    return cricketers

def search(query):
    choices= [u"වැඩිම ලකුණු ලබාගත් ක්‍රීඩකයන්",u"වැඩිම කඩුලු ලබාගත් ක්‍රීඩකයන්",u"වැඩිම තරඟ ක්‍රීඩා කළ ක්‍රීඩකයන්"]
    highest = process.extractOne(u'%s' % query, choices, scorer=fuzz.ratio)
    if(highest[1]>50):
        results = post_processing(top_search(query))
    else:
        results = post_processing(keyword_search(query))
    return results

# if __name__ == "__main__":
#     print(search("පිතිකරු"))

# fields = ["id","Full Name","Born","Age","Batting Style","Bowling Style","Playing Role","Education","Matches","Runs","Average","Half-centuries",
# "Centuries","Wickets","Economy","Player Bio","Full Name si"]