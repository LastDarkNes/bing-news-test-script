import json
from pprint import pprint
import requests

# Parse settings
settings = dict()
with open('./settings.json') as json_settings:
    payload = ""
    for i in json_settings:
        payload += i
    settings = json.loads(payload)

# Set up bing params
subscription_key = settings['api_key']
endpoint = settings['url'] + settings['endpoint']

# Set up request params
params = settings["query_params"]
headers = {'Ocp-Apim-Subscription-Key': subscription_key}

# Call the API & Print result
try:
    response = requests.get(endpoint, headers=headers, params=params)

    print(response.url)
    response.raise_for_status()

    print("Headers:")
    print(response.headers)

    print("JSONResponse:")
    pprint(response.json())

except Exception as ex:
    pprint(response.json())

    raise ex
