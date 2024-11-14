import requests


raw = requests.get("https://the-trivia-api.com/v2/questions")
data = raw.json()
print(data)






