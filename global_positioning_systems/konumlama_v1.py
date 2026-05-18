from paramDic_2 import GNSS_trilaterasyon as konumlama
from paramDic_2 import GNSS
from paramDic_2 import ecef_to_geodetic
import numpy as np
from numpy.linalg import inv

# Veriler
GIRS_coor= np.array([[3782947.6300],
                [2997054.3943],
                [4155987.9551]])
lat,lon,h=ecef_to_geodetic(GIRS_coor[0].item(),GIRS_coor[1].item(),GIRS_coor[2].item())

Sat_coor=np.array([[[-13208226.7323],[12676318.4734],[18766611.3563]],
                   [[24591676.7017],[-9846611.4955],[889654.7808]],
                   [[22307430.0348],  [12429753.2552],  [7506301.6570]],
                   [[-2310744.6865],  [17095144.7411],  [20169897.9631]],
                   [[23354607.6507],  [626266.8878],  [12410086.8113]],
                   [[8715351.0521], [19765674.2915],  [15810873.7736]],
                   [[15600686.3730],  [19920374.9785],  [8360003.3354]],
                   [[14594131.6925], [-8293755.5055],  [20135255.3410]]])
pseudoranges= np.array([[24356738.594],
                        [24787074.094],
                        [20895895.867],
                        [22161314.664],
                        [21358234.984],
                        [20792991.766],
                        [20965804.516],
                        [22421540.469]])
# UYDU ACİLARİ 
R=GNSS.R2enu(lat,lon)
uydu_acilari = GNSS.tum_uydulari_hesapla(Sat_coor, GIRS_coor[0].item(),GIRS_coor[1].item(),GIRS_coor[2].item())

# DOP DEGERLERİNİN HESAPLANMASI
Sat_coor=np.array([[-13208226.7323,12676318.4734,18766611.3563],
                   [24591676.7017,-9846611.4955,889654.7808],
                   [22307430.0348,  12429753.2552,  7506301.6570],
                   [-2310744.6865,  17095144.7411,  20169897.9631],
                   [23354607.6507,  626266.8878,  12410086.8113],
                   [8715351.0521, 19765674.2915,  15810873.7736],
                   [15600686.3730, 19920374.9785,  8360003.3354],
                   [14594131.6925, -8293755.5055,  20135255.3410]])
GIRS_coor= np.array([3782947.6300,2997054.3943,4155987.9551])
GDOP, PDOP,HDOP,VDOP,TDOP=GNSS.ecef_to_DOP(Sat_coor,GIRS_coor)

# KONUMLAMA
A,W,xCap,yCap,zCap,deltaX,deltaY,deltaZ= GNSS.kartezyen_konumlama(Sat_coor,float(GIRS_coor[0].item()),float(GIRS_coor[1].item()),float(GIRS_coor[2].item()),pseudoranges,3)
