import requests

URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

def get_wiki_page():
    with requests.get(URL) as response:
        if response.status_code != 200:
            # response.raise_for_status()
            raise Exception(
                'response code is : {}'.format(response.status_code))
        return response.json()
