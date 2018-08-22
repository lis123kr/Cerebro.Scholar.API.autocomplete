import json
import elastic_search


def main(event, context):
    params = event['query']
    result = elastic_search.get(keyword=params["keyword"], size=int(params["size"]), is_suggest=bool(params.get("is_suggested")))

    body = {
        "message": json.dumps(result),
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
