import requests

def fetch_a_word() -> str:
    url = "https://wordsapiv1.p.rapidapi.com/words/"

    querystring = {"random":"true"}

    headers = {
        "X-RapidAPI-Key": "9414b4c9b4mshaa5d862512c2150p1739a8jsn85642a2e29d2",
        "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    return response.json()["word"]
