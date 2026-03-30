import numpy as np
from numpy.linalg import inv
import math

sta_ecef = np.array([4124040.844, 2655252.244, 4065430.231])

sats_ecef = np.array([
    [ 5609448.760,  25140132.527,   6372861.822],
    [12105770.780,  23015761.543,  -5496104.244],
    [19650283.614,  -4485204.994,  16977216.177],
    [20485152.071,  13348417.187, -10775266.255],
    [26018028.018,   3827960.254,  -5138658.487],
    [-7031440.559,  13781275.560,  22038514.691],
    [ 5500349.320,  15674107.329,  20551836.203],
    [18243998.969,   6311666.767,  18084027.214],
    [19496813.820, -15213836.485,   9008928.532],
    [ 2838903.927, -15089793.387,  21815968.274]
])

def ecef_to_geodetic(x, y, z):
    a = 6378137.0
    b = 6356752.3142
    e2 = (a**2 - b**2) / a**2
    ep2 = (a**2 - b**2) / b**2
    
    p = math.sqrt(x**2 + y**2)
    th = math.atan2(a * z, b * p)
    
    lon = math.atan2(y, x)
    lat = math.atan2(z + ep2 * b * math.sin(th)**3, p - e2 * a * math.cos(th)**3)
    return lat, lon

lat, lon = ecef_to_geodetic(sta_ecef[0], sta_ecef[1], sta_ecef[2])

sinP, cosP = math.sin(lat), math.cos(lat)
sinL, cosL = math.sin(lon), math.cos(lon)

R_enu = np.array([
    [-sinL,           cosL,           0   ],  # East
    [-sinP * cosL,   -sinP * sinL,    cosP],  # North
    [ cosP * cosL,    cosP * sinL,    sinP]   # Up
])

A_list = []
for sat in sats_ecef:
  
    dx = sat[0] - sta_ecef[0]
    dy = sat[1] - sta_ecef[1]
    dz = sat[2] - sta_ecef[2]
    rho = math.sqrt(dx**2 + dy**2 + dz**2)
    
    ax = -dx / rho
    ay = -dy / rho
    az = -dz / rho
    
    A_list.append([ax, ay, az, 1])

A = np.array(A_list)

Q = inv(A.T @ A)

Q_xyz = Q[:3, :3]

Q_enu = R_enu @ Q_xyz @ R_enu.T

GDOP = math.sqrt(np.trace(Q))
PDOP = math.sqrt(np.trace(Q_xyz))
HDOP = math.sqrt(Q_enu[0, 0] + Q_enu[1, 1])  
VDOP = math.sqrt(Q_enu[2, 2])                
TDOP = math.sqrt(Q[3, 3])                    

print(f"{'DOP DEĞERLERİ'}")
print(f"GDOP : {GDOP}")
print(f"PDOP : {PDOP}")
print(f"HDOP : {HDOP}")
print(f"VDOP : {VDOP}")
print(f"TDOP : {TDOP}")
