"""
Created by hangeonho on 2018. 8. 22..
"""


def get(keyword, size, is_suggest):
    if is_suggest:
        query = {
            "size": size,
            "suggest": {
                "autocomp": {
                    "text": keyword,
                    "completion": {
                        "field": "keyword.completion"
                    }
                }
            }
        }
    else:
        query = {
            "size": size,
            "query": {
                "match_phrase_prefix": {
                    "keyword.two_word": {
                        "query": keyword,
                        "max_expansions": 10
                    }
                }
            },
            "sort": [
                {
                    "keyDetected": {
                        "order": "desc"
                    }
                }
            ]
        }
    return query
