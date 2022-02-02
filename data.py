import requests

parametrs = {
    "amount":20,
    "type":"boolean"
}
respones = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean",params=parametrs)
respones.raise_for_status()
data = respones.json()
question_data = data["results"]
