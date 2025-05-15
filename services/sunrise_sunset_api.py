from typing import Optional
import requests


class SunriseSunsetAPI:

    BASE_URL = "https://api.sunrise-sunset.org/json"

    def fetch_data(self, latitude: float, longitude: float) -> Optional[dict]:
        """
        Faz uma requisição GET para a API
        e retorna o Json como um dicionário.
        returns:
            dict: Dados JSON retornados pela API
        """
        url = (
            f'https://api.sunrise-sunset.org/json?lat={latitude}'
            f'&lng={longitude}&date=today&formatted=0'
        )
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                print('Erro ao acessar a API')
                return None
        except requests.exceptions.RequestException as e:
            print(f'Error: {e}')
            return None
