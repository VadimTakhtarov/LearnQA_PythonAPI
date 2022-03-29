import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect",)
print(f"Redirect count: {len(response.history)}")
print(f"Last request URL: {response.url}")