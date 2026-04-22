import requests
from config.settings import API_URL


def get_questions():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()

    data = response.json()

    if data["response_code"] != 0:
        raise ValueError("Could not get questions from the API.")

    return data["results"]