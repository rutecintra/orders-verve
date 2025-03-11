import requests
import logging
from src.integrations.models import Integrations

class BaseIntegrationService:
    def __init__(self, integration_title):
        self.integration_title = integration_title
        self.integration = self.get_credentials()
        self.api_key = self.integration.get("api_key") if self.integration else None
        self.api_url = self.integration.get("api_url") if self.integration else None

        if not self.api_key or not self.api_url:
            logging.error(f"Error loading integration credentials: {integration_title}")
        
        self.headers = {
            "Authorization": self.api_key,
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def get_credentials(self):
        try:
            integration = Integrations.objects.get(title=self.integration_title)
            return {
                "api_key": integration.apikey,
                "api_url": integration.apiurl
            }
        except Integrations.DoesNotExist:
            logging.error(f"Credentials not found: {self.integration_title}")
            return None

    def request(self, method, endpoint, params=None, data=None):
        if not self.api_key or not self.api_url:
            logging.error("API Key or URL undefined.")
            return None

        url = f"{self.api_url}/api/{endpoint}"
        headers = {"Authorization": self.api_key, "Content-Type": "application/json"}

        try:
            response = requests.request(method, url, headers=headers, params=params, json=data)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error to do {method.upper()} on {url}: {e}")
            return None

    def get(self, endpoint, params=None):
        return self.request("GET", endpoint, params=params)

    def post(self, endpoint, data):
        return self.request("POST", endpoint, data=data)

    def put(self, endpoint, data):
        url = f"{self.base_url}/api/{endpoint}"
        try:
            response = requests.put(url, headers=self.headers, json=data)
            response.raise_for_status()
            logging.info(f"PUT {url} - Order updated!")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error updating order {url}: {e}")
            return None

    def delete(self, endpoint):
        return self.request("DELETE", endpoint)