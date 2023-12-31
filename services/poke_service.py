import requests

class RequestSender:
    def __init__(self, service_url):
        self.service_url = service_url

    def send_request(self, attributes):
        url = f"{self.service_url}/find_similar"
        response = requests.post(url, json=attributes)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Request failed with status code {response.status_code}")
            return None
            