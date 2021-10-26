from elasticsearch import Elasticsearch, helpers
import json
import re

es = Elasticsearch([{'host': '127.0.0.1', 'port':9200}])

def keyword_search(query):
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

    print(results)
    # Full_Name, Batting_Style, Player_Bio  = post_processing(results)
    return results

def post_processing(results):
    actors = []
    for i in range(len(results['hits']['hits'])):
        # lyrics = json.dumps(results['hits']['hits'][i]['_source']["name"], ensure_ascii=False)
        # lyrics = lyrics.replace('"', '')
        # lyrics = lyrics.replace("'", '')
        # lyrics = lyrics.replace('\\', '')
        # lyrics = lyrics.replace('t', '')
        # lyrics = lyrics.replace('\xa0', '')
        # lyrics = "<br>".join(lyrics.split("n"))
        # lyrics = re.sub(r'(<br> )+', r'\1', lyrics)
        # j = 0
        # while True:
        #     if lyrics[j] == '<' or lyrics[j] == '>' or lyrics[j] == 'b' or lyrics[j] == 'r' or lyrics[j] == ' ':
        #         j += 1
        #     else:
        #         break
        # lyrics = lyrics[j:]
        # results['hits']['hits'][i]['_source']["song_lyrics"] = lyrics
        actors.append(results['hits']['hits'][i]['_source'])
    aggregations = results['aggregations']
    names = aggregations['name']['buckets']
    real_names = aggregations['real_name']['buckets']
    birthdays = aggregations['birthday']['buckets']
    diedes = aggregations['died']['buckets']
    addresses = aggregations['address']['buckets']

    return actors,names, real_names, birthdays, diedes, addresses

def search(query):
    results = keyword_search(query)
    return results

# if __name__ == "__main__":
#     print(search("පිතිකරු"))

# fields = ["id","Full Name","Born","Age","Batting Style","Bowling Style","Playing Role","Education","Matches","Runs","Average","Half-centuries",
# "Centuries","Wickets","Economy","Player Bio","Full Name si"]