import requests

DDG_BASE_API_URL = "https://api.duckduckgo.com"

FETCH_PRESIDENTS_QUERY = "presidents of the united states"


def fetch_presidents():
    apiRequestUrl = f"{DDG_BASE_API_URL}/?q={FETCH_PRESIDENTS_QUERY}&format=json"

    response = requests.get(apiRequestUrl)
    response_data = response.json()

    presidents = []

    for relatedTopic in response_data["RelatedTopics"]:
        presidentLastName = relatedTopic["Text"].split(
            "-")[0].strip().split(" ")[-1]

        presidents.append(presidentLastName)

    return presidents
