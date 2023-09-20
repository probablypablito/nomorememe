import os
import json
import requests,requests_cache
import httpx



subscription_key = os.environ['subscription_key']
endpoint = 'https://api.bing.microsoft.com/v7.0' + "/images/search"
mkt = 'en-US'
headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

requests_cache.install_cache('api_cache', expire_after=604800)

async def getImage(query):

    params = { 'q': query, 'mkt': mkt, 'count': 1 }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(endpoint, params=params, headers=headers)

            response.raise_for_status()

            images = response.json()['value']
            url = images[0]['contentUrl']
            image_response = await client.get(url)
            return image_response.content

        except httpx.HTTPError as e:
            raise Exception(f"HTTP error occurred: {e}")
        except Exception as e:
            raise Exception(f"An error occurred: {e}")