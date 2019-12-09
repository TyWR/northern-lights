import urllib3
from .util.etl import read_power, read_time

def get_aurora_power():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    http = urllib3.PoolManager()
    url  = 'https://services.swpc.noaa.gov/text/aurora-nowcast-map.txt'
    res  = http.request('GET', url)
    return read_power(res.data)

def get_time():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    http = urllib3.PoolManager()
    url = 'https://services.swpc.noaa.gov/text/aurora-nowcast-map.txt'
    res = http.request('GET', url)
    return read_time(res.data)
