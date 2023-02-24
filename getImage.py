import os
import json
import requests,requests_cache

subscription_key = os.environ['subscription_key']
endpoint = 'https://api.bing.microsoft.com/v7.0' + "/images/search"
mkt = 'en-US'
headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

requests_cache.install_cache('api_cache', expire_after=3600)



def getImage(query):

    # Construct a request
    params = { 'q': query, 'mkt': mkt, 'count': 1 }

    # Call the API
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()
        images = response.json()['value']
        url = images[0]['contentUrl']
        return requests.get(url).content
    
    except RuntimeError:
        raise 'Getting image failed. Maybe no results?'
    