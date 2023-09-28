import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        response_body = self.get_response_body()
        try:
            return json.loads(response_body)
        except json.JSONDecodeError:
            print(f"Error decoding JSON data from {self.url}")
            return None
