"""
Created by hangeonho on 2018. 8. 22..
"""
import elastic_search


def test_get():
    print("hello world!")
    print(elastic_search.get(keyword="ma", size=6, is_suggest=True))
