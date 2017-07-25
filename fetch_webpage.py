import requests


def fetch_webpage(url):
    return requests.get(url).text
