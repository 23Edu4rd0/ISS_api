import requests
from typing import Optional


class iss_api:
    """
    Classe para acessar a API do ISS

    Returns:
        dict: Dados JSON retornados pela API
    """

    BASE_URL = 'http://api.open-notify.org/iss-now.json'

    def fetch_data(self) -> Optional[dict]:
        try:
            response = requests.get(self.BASE_URL)
            if response.status_code == 200:
                return response.json()
            else:
                print('Erro ao acessar a API')
                return None
        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')
            return None
