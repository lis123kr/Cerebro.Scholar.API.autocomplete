"""
Created by hangeonho on 2018. 8. 22..
"""
import requests
import json
import query


def get(keyword, size, is_suggest):
    return request(keyword=keyword, size=size, is_suggest=is_suggest)


def request(keyword, size, is_suggest):
    URL = 'https://fd2b16254da343159c56f09ad393c420.us-west-1.aws.found.io:9243/tags/words/_search'
    headers = {'Accept': 'text/plain', 'Content-type': 'application/json'}
    result = requests.get(URL, data=json.dumps(query.get(size=size, keyword=keyword, is_suggest=is_suggest)), headers=headers, auth=('elastic', 'Ftkn0jSUxwI867OzNmPiAVeu'))

    if not is_suggest:
        hits = json.loads(result.text)['hits']['hits']
        if len(hits) > 0:
            return [h['_source']['keyword'] for h in hits]
    else:
        hits = json.loads(result.text)['suggest']['autocomp'][0]
        if len(hits) > 0:
            return [h['text'] for h in hits['options']]
    return []
