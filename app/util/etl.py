import re
import numpy as np
import itertools

def read_power(raw):
    """Parses raw txt geodata. It returns the power along longitude and
    latitude with the validity time. It also returns an array containing
    the latitudes and longitudes vector."""

    lines = raw.split(b"\n")
    headsize, size = 17, 512    # Head and total number of lines
    header, lines = lines[:headsize], lines[headsize: size + headsize]

    dec_long, dec_lat = 2, 2
    long  = np.linspace(-180, 180, 1024//dec_long)
    lat   = np.linspace(-90, 90, 512//dec_lat)
    power = np.loadtxt(lines, dtype=np.dtype(int))
    power = power[0:512:dec_lat, 0:1024:dec_long]
    indices = np.nonzero(power)
    print("Total values considered:", indices[0].shape)
    out = {"points": []}
    for p, long, lat in zip(
            power[indices].flatten().tolist(),
            long[indices[1]].tolist(),
            lat[indices[0]].tolist()):
        if lat < 84 and lat > -80:
            out["points"].append({
                "power": p,
                "x"    : long,
                "y"    : lat
            })
    return out

def read_time(raw):
    lines = raw.split(b"\n")
    headsize, size = 17, 512    # Head and total number of lines
    header, lines = lines[:headsize], lines[headsize: size + headsize]

    match = re.search(b'\d{4}-\d{2}-\d{2} \d{1,2}:\d{2}', header[2])
    time = match.group(0).decode('utf-8')
    return time
