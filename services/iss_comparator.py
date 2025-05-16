from datetime import datetime
from models.location import MyLocation
from models.iss_location import IssLocation


class ISSComparator:
    def __init__(self, my_lat: float = -20.140373, my_lon: float = -44.868309):
        self.my_location = MyLocation(my_lat, my_lon)
        self.iss = IssLocation()

    def get_iss_data(self):
        location = self.iss.get_iss_location()
        lat = self.iss.get_iss_latitude(location)
        lon = self.iss.get_iss_longitude(location)
        return lat, lon

    def get_sun_times(self):
        return self.my_location.get_sunrise(), self.my_location.get_sunset()

    def get_my_location(self):
        return self.my_lat, self.my_lon

    def compare(self, proximity_deg: float = 5.0):
        """
        Compara a localização da ISS com a localização do usuário.

        Args:
            proximity_deg (float, optional): Diferença máxima (em graus)
            permitida entre a latitude e longitude da ISS e a do usuário para
            considerar que a ISS está "próxima" da sua localização.
            O valor padrão é 5.0 porque, devido à altitude da ISS (~400 km)
            e ao seu brilho intenso, ela pode ser vista a olho nu
            em uma área relativamente ampla do céu,
            mesmo que não esteja exatamente sobre a sua cidade.
            Esse valor é uma escolha comum em projetos e sites de rastreamento
            da ISS para balancear precisão e praticidade:
            valores maiores tornam o critério mais permissivo
            (considerando a ISS visível em uma área maior),
            enquanto valores menores tornam o critério mais restrito.

        Returns:
            bool: True se a ISS estiver próxima e for noite.
            False caso contrário.
        """
        iss_lat, iss_lon = self.get_iss_data()
        my_sunrise, my_sunset = self.get_sun_times()
        my_lat, my_lon = self.get_my_location()

        if (
            iss_lat and
            iss_lon and
            my_sunrise and
            my_sunset
        ):
            iss_lat = float(iss_lat)
            iss_lon = float(iss_lon)
            my_lat = float(my_lat)
            my_lon = float(my_lon)

            is_near = (
                abs(iss_lat - my_lat) < proximity_deg and
                abs(iss_lon - my_lon) < proximity_deg
            )

            now_hour = datetime.now().strftime('%H')

            is_night = (
                now_hour < my_sunrise or now_hour > my_sunset
            )

            if is_near and is_night:
                return True
            else:
                return False
