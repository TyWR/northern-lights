from .etl import parser
import urllib3

def get_aurora_power():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    http = urllib3.PoolManager()
    url  = 'https://services.swpc.noaa.gov/text/aurora-nowcast-map.txt'
    res  = http.request('GET', url)
    return parser(res.data)
