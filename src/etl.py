import re
import numpy as np
import itertools
import pandas as pd

def parser(raw):
    """Parses raw txt geodata. It returns the power along longitude and
    latitude with the validity time. It also returns an array containing
    the latitudes and longitudes vector."""

    lines = raw.split(b"\n")
    headsize, size = 17, 512    # Head and total number of lines
    header, lines = lines[:headsize], lines[headsize: size + headsize]

    match = re.search(b'\d{4}-\d{2}-\d{2} \d{1,2}:\d{2}', header[2])
    time = match.group(0).decode('utf-8')

    dec = 8
    long = np.linspace(-180, 180, 1024//dec)
    lat  = np.linspace(-90, 90, 512//dec)
    power = np.array([
        [int(x) for i, x in enumerate(line.decode('utf-8').split())
            if not i%dec]
        for j, line in enumerate(lines) if not j%dec
    ])
    indices = np.nonzero(power)
    print("Total values considered:", indices[0].shape)

    out = {
        "power"     : power[indices].flatten(),
        "longitude" : long[indices[1]],
        "latitude"  : lat[indices[0]]
    }

    return pd.DataFrame(out), time
