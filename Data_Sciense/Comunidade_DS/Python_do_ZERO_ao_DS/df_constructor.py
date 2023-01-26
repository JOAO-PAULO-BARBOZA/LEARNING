from time import sleep
from geopy.geocoders import Nominatim

# Criação do geo_locator
geo_locator = Nominatim(user_agent="geoTantoFaz")

def get_data(x): 
    index, row = x
    sleep(1)
    # Chamada da API
    response = geo_locator.reverse(row['location'])

    address = response.raw['address']
    place_id = response.raw['place_id']
    osm_type = response.raw['osm_type']
    country = address['country']
    country_code = address['country_code']
    
    return place_id, osm_type, country, country_code
