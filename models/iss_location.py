from services.iss_api import iss_api
from typing import Optional


class IssLocation:

    def __init__(self):
        self.api = iss_api()

    def get_iss_location(self) -> Optional[dict]:
        """
        Obtem a localização atual do ISS

        Returns:
            Optional[dict]: Localização do ISS
        """
        data = self.api.fetch_data()
        if data and 'iss_position' in data:

            return data
        return None

    def get_iss_latitude(self, data: Optional[dict]) -> Optional[str]:
        """
        Obtem a latitude do ISS

        Args:
            data (Optional[dict]): Dict com a posição atual do ISS

        Returns:
            Optional[str]: Latitude do ISS duh
        """
        if (
            data and
            'iss_position' in data and
            'latitude' in data['iss_position']
        ):
            return data['iss_position']['latitude']
        return None

    def get_iss_longitude(self, data: Optional[dict]) -> Optional[str]:
        """
        Obtem a longitude do ISS

        Returns:
            Optional[str]: Longitude do ISS duhhh
        """
        if (
            data and
            'iss_position' in data and
            'longitude' in data['iss_position']
        ):
            return data['iss_position']['longitude']
        return None

    def get_iss_timestamp(self, data: Optional[dict]) -> Optional[int]:
        """
        Obtem o timestamp do Iss

        Args:
            data (Optional[dict]): dicionario completo retornado pela API

        Returns:
            Optional[int]: Timestamp do ISS duhhhhhh
        """

        if data and 'timestamp' in data:
            return data['timestamp']
        return None
