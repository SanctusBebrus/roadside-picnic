import requests
from math import sin, cos, sqrt, atan2, radians


def get_geo_info(city, type_info):
    def get_coordinates(city_name):
        url = "https://geocode-maps.yandex.ru/1.x/"

        params = {
            'geocode': city_name,
            'format': 'json',
            'apikey': "40d1649f-0493-4b70-98ba-98533de7710b"
        }

        response = requests.get(url, params)
        json = response.json()
        point_str = json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
        point_array = [float(x) for x in point_str.split(' ')]

        return point_array

    def get_country(city_name):
        url = "https://geocode-maps.yandex.ru/1.x/"

        params = {
            'geocode': city_name,
            'format': 'json',
            'apikey': "40d1649f-0493-4b70-98ba-98533de7710b"
        }

        response = requests.get(url, params)
        json = response.json()

        return \
            json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty'][
                'GeocoderMetaData'][
                'AddressDetails']['Country']['CountryName']

    if type_info == 'country':
        get_country(city)
    elif type_info == 'coordinates':
        get_coordinates(city)


def get_distance(p1, p2):
    R = 6373.0

    lon1 = radians(p1[0])
    lat1 = radians(p1[1])
    lon2 = radians(p2[0])
    lat2 = radians(p2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c

    return distance
