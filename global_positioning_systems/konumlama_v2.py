from paramDic_2 import deltaCap_standart, Cr_, dms_to_radian, xCap
from paramDic_2 import GNSS_trilaterasyon as konumlama
from paramDic_2 import GNSS
from paramDic_2 import ecef_to_geodetic
import numpy as np
from numpy.linalg import inv
import paramDic_2
import math

# Veriler
lat = 39.0
lon = 30.0
h = 1000.0
X, Y, Z = paramDic_2.geodetic_to_ecef(lat, lon, h)
recv_coor = np.array([[X], [Y], [Z]])

Sat_coor=np.array([
    [ [15483704.907], [4291236.535], [19966556.765] ],
    [[6963767.996], [8910990.150], [21214948.604]],
    [[17144509.155], [-9879352.949], [12468711.396]],
    [[10801779.303], [22664639.601], [-346547.608]],
    [[14981670.526], [-13406040.750], [10725837.817]],
    [[19096453.795], [14302362.866], [12268186.638]],
    [[ 18981860.770] ,[14707284.339], [13490996.501]],
    [[14308626.738], [5615519.874], [19578204.448]],
    [[19135856.558], [-5575633.645], [17154529.082]],
    [ [-7822806.434], [9989892.320], [17797054.899]]
])
pseudoranges= np.array([
        [19584066.939], 
        [18944319.793], 
        [19129197.155], 
        [21643796.134], 
        [20295500.251], 
        [20675932.684], 
        [21336692.926], 
        [18785921.035], 
        [21407584.406], 
        [19845912.701]  
    ])

# UYDU ACİLARİ 
R=GNSS.R2enu(lat,lon)
uydu_acilari = GNSS.tum_uydulari_hesapla(Sat_coor, recv_coor[0].item(),recv_coor[1].item(),recv_coor[2].item())

# DOP DEGERLERİNİN HESAPLANMASI
recv_coor= np.array([X,Y,Z])
Sat_coor=np.array([
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
GDOP, PDOP,HDOP,VDOP,TDOP=GNSS.ecef_to_DOP(Sat_coor,recv_coor)

# KONUMLAMA
A,W,xCap,yCap,zCap,deltaX,deltaY,deltaZ= GNSS.kartezyen_konumlama(Sat_coor,float(recv_coor[0].item()),float(recv_coor[1].item()),float(recv_coor[2].item()),pseudoranges,3)
