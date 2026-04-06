from paramDic_2 import deltaCap_standart, Cr_, dms_to_radian, xCap
from paramDic_2 import deltaCap_standart, Cr_, dms_to_radian, xCap
from paramDic_2 import GNSS_trilaterasyon as konumlama
from paramDic_2 import GNSS
from paramDic_2 import geodetic_to_ecef
import numpy as np
from numpy.linalg import inv
import math

ANK_angle=np.array([[40],
                    [33]])

R = GNSS.R2enu(ANK_angle[0].item(), ANK_angle[1].item())
x,y,z=geodetic_to_ecef(ANK_angle[0].item(),ANK_angle[1].item(),0)

Sat_coor=np.array([[[3843219.1176], [-16635600.4107],  [-20556083.9992]],
                   [[587530.0028], [-26281259.6699 ], [3393272.3014]],
                   [[-12660602.5049],[  -10764921.7942], [ 21227336.5316]],
                   [[23553858.9652], [ 10696530.3354 ], [-6556890.7665]],
                   [[-12985686.5465],[  19287151.5279 ],[ 12491300.1659]],
                   [[14221911.4840], [-7090656.1957 ], [21076904.7080]],
                   [[-15423306.4305], [ 2769590.6865 ], [-21642469.4752]],
                   [[ 15353869.4421 ],[ -6398867.7037 ],[ -20246852.5371]],
                   [[14218238.4720],  [19512255.0996 ], [-11670952.0798]],
                   [[22474726.6767],  [4701888.0401 ], [13296320.8112]],
                   [[25204330.9684 ], [-5711889.7559 ],[ -7250385.1216]]
                   ])
gorunen_uydu = GNSS.gorur_gormez_analizi(Sat_coor, x,y,z, R)

sat_poz=np.array([[[23553858.9652], [ 10696530.3354 ], [-6556890.7665]],
                  [[-12985686.5465],[  19287151.5279 ],[ 12491300.1659]],
                  [[14221911.4840], [-7090656.1957 ], [21076904.7080]],
                  [ [14218238.4720],  [19512255.0996 ], [-11670952.0798]],
                  [[22474726.6767],  [4701888.0401 ], [13296320.8112]],
                  [[25204330.9684 ], [-5711889.7559 ],[ -7250385.1216]]])

# DOP DEGERLERİNİN HESAPLANMASI
GDOP, PDOP,HDOP,VDOP,TDOP=GNSS.uydu_DOP(gorunen_uydu,x,y,z,R)

