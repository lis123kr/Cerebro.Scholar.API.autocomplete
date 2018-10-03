"""
Created by hangeonho on 2018. 8. 22..
"""
import requests
import json
import query


def get(keyword, size, is_suggest):
    return request(keyword=keyword, size=size, is_suggest=is_suggest)


def request(keyword, size, is_suggest):
    URL = 'http://113.198.137.239:9200/tags/words/_search'
    headers = {'Accept': 'text/plain', 'Content-type': 'application/json'}

    http_proxy  = "http://113.198.137.239:8080"
    https_proxy  = "https://113.198.137.239:8080"
    proxyDict = { 
        "http"  : http_proxy,
        "https" : https_proxy
     }

    result = requests.post(URL, data=json.dumps(query.get(size=size, keyword=keyword, is_suggest=is_suggest)), 
        headers=headers, proxies=proxyDict)

    if not is_suggest:
        hits = json.loads(result.text)['hits']['hits']
        if len(hits) > 0:
            return [h['_source']['keyword'] for h in hits]
    else:
        hits = json.loads(result.text)['suggest']['autocomp'][0]
        if len(hits) > 0:
            return [h['text'] for h in hits['options']]
    return []
