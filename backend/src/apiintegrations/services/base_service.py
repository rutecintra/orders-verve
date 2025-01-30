import requests
import logging
from django.utils.dateparse import parse_datetime
from src.integrations.models import Integrations

class BaseIntegrationService:
    def __init__(self, integration_title):
        self.integration = self.get_credentials(integration_title)
        if self.integration:
            self.api_key = self.integration["api_key"]
            self.api_url = self.integration["api_url"]
        else:
            logging.error(f"Erro ao carregar credenciais da integração: {integration_title}.")
            self.api_key = None
            self.api_url = None

    def get_credentials(self, integration_title):
        try:
            integration = Integrations.objects.get(title=integration_title)
            return {
                "api_key": integration.apikey,
                "api_url": integration.apiurl
            }
        except Integrations.DoesNotExist:
            return None

    def get(self, endpoint):
        """Faz uma requisição GET para a API da integração"""
        if not self.api_key or not self.api_url:
            logging.error("API Key ou URL não definida.")
            return None

        headers = {"Authorization": self.api_key}
        try:
            response = requests.get(f"{self.api_url}/{endpoint}", headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Erro ao buscar dados: {e}")
            return None

    def put(self, endpoint, data):
        """Faz uma requisição PUT para a API da integração"""
        if not self.api_key or not self.api_url:
            logging.error("API Key ou URL não definida.")
            return None

        headers = {"Authorization": self.api_key, "Content-Type": "application/json"}
        try:
            response = requests.put(f"{self.api_url}/{endpoint}", json=data, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Erro ao enviar dados: {e}")
            return None