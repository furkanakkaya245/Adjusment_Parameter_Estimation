import numpy as np
from numpy.linalg import inv
import math
from paramDic_2 import GNSS
import paramDic_2

lat = 39.0
lon = 30.0
h = 1000.0

X, Y, Z = paramDic_2.geodetic_to_ecef(lat, lon, h)

nok_koor = np.array([X, Y, Z])


sats_ecef = np.array([
    [ 15483704.907, 4291236.535, 19966556.765 ],
    [6963767.996, 8910990.150, 21214948.604],
    [17144509.155, -9879352.949, 12468711.396],
    [10801779.303, 22664639.601, -346547.608],
    [14981670.526, -13406040.750, 10725837.817],
    [19096453.795, 14302362.866, 12268186.638],
    [ 18981860.770 ,14707284.339, 13490996.501],
    [14308626.738, 5615519.874, 19578204.448],
    [19135856.558, -5575633.645, 17154529.082],
    [ -7822806.434, 9989892.320, 17797054.899]
])

GDOP, PDOP, HDOP, VDOP, TDOP= GNSS.ecef_to_DOP(sats_ecef, nok_koor)




