from elasticsearch.helpers import streaming_bulk
from elasticsearch import Elasticsearch, helpers
import json
import tqdm

es = Elasticsearch([{'host': '127.0.0.1', 'port':9200}])

def indexing():
    with open('cricketers.json', encoding='utf8') as f:
        data = json.loads(f.read())
    # print(data)
    # helpers.bulk(es, data, index='index-actors')
    es.indices.create(
        request_timeout=60,
        index="index-cricketers",
        body={
            "settings": {"number_of_shards": 1},
            "mappings": {
                "properties": {
                    "Full_Name": {"type": "text"},
                    "Full_Name_si": {"type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                },
                                },
                    "Born": {"type": "text",
                                     "fields": {
                                         "keyword": {
                                             "type": "keyword"
                                         }
                                     },
                                     },
                    "Age": {"type": "text",
                                    "fields": {
                                        "keyword": {
                                            "type": "keyword"
                                        }
                                    },
                                    },
                    "Education": {"type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                },
                                },
                    'Matches': {"type": "text"},
                    'Runs': {"type": "text"},
                    'Average': {"type": "text"},
                    'Half-centuries': {"type": "text"},
                    'Centuries': {"type": "text"},
                    'Wickets': {"type": "text"},
                    'Economy': {"type": "text"},
                    "Player_Bio": {"type": "text",
                                "fields": {
                                    "keyword": {
                                        "type": "keyword"
                                    }
                                },
                                },
                }
            },
        },
        ignore=400,
    )
    progress = tqdm.tqdm(unit="docs", total=100)
    successes = 0
    for ok, action in streaming_bulk(
            client=es, index="index-cricketers", actions=data,
    ):
        progress.update(1)
        successes += ok
    print("Indexed %d/%d documents" % (successes, 10))


if __name__ == "__main__":
    indexing()
