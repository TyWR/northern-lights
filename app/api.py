import requests
from .util.etl import read_power, read_time

def get_aurora_power():
    url  = 'https://services.swpc.noaa.gov/text/aurora-nowcast-map.txt'
    res  = requests.get(url)
    return read_power(res.content)

def get_time():
    url = 'https://services.swpc.noaa.gov/text/aurora-nowcast-map.txt'
    res = requests.get(url)
    return read_time(res.content)
