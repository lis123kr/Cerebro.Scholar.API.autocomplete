import json
import elastic_search


def main(event, context):
    params = event['queryStringParameters']
    result = elastic_search.get(keyword=params["keyword"], size=int(params["size"]), is_suggest=bool(params.get("is_suggested")))

    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }

    return response
