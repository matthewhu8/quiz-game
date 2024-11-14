"""
This module fetches trivia questions from an external API.
"""

import requests

raw = requests.get("https://the-trivia-api.com/v2/questions")
data = raw.json()
print(data)
