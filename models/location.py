from services.sunrise_sunset_api import SunriseSunsetAPI


class MyLocation:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude

    def get_sun_time(self) -> str:
        """
        Obtém o horário do nascer do sol

        Returns:
            str: Horário do nascer do sol
        """
        data = SunriseSunsetAPI().fetch_data(self.latitude, self.longitude)
        if data and 'results' in data:
            sunrise = data['results']['sunrise']
            sunset = data['results']['sunset']
            return {'sunrise': sunrise, 'sunset': sunset}
        print('Erro ao obter os dados')
        return None

    def get_sunrise(self) -> str:
        times = self.get_sun_time()
        if times:
            return times['sunrise'].split('T')[1].split(':')[0]
        return None

    def get_sunset(self) -> str:
        """
        Obtém o horário do pôr do sol

        Returns:
            str: Horário do pôr do sol
        """
        times = self.get_sun_time()
        if times:
            return times['sunset'].split('T')[1].split(':')[0]
        return None
