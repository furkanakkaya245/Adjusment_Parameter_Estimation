from paramDic_2 import GNSS
from paramDic_2 import geodetic_to_ecef
import numpy as np

ANK_angle = np.array([40.0, 33.0])

x, y, z = geodetic_to_ecef(ANK_angle[0], ANK_angle[1], 0)

rcv_coor = np.array([x, y, z]) 

Sat_coor = np.array([
    [ 3843219.1176, -16635600.4107, -20556083.9992],
    [  587530.0028, -26281259.6699,   3393272.3014],
    [-12660602.5049, -10764921.7942,  21227336.5316],
    [ 23553858.9652,  10696530.3354,  -6556890.7665],
    [-12985686.5465,  19287151.5279,  12491300.1659],
    [ 14221911.4840,  -7090656.1957,  21076904.7080],
    [-15423306.4305,   2769590.6865, -21642469.4752],
    [ 15353869.4421,  -6398867.7037, -20246852.5371],
    [ 14218238.4720,  19512255.0996, -11670952.0798],
    [ 22474726.6767,   4701888.0401,  13296320.8112],
    [ 25204330.9684,  -5711889.7559,  -7250385.1216]
])
gorunen_uydular = GNSS.gorur_gormez_analizi(Sat_coor, x, y, z)
if len(gorunen_uydular) >= 4:
    GDOP, PDOP, HDOP, VDOP, TDOP = GNSS.ecef_to_DOP(gorunen_uydular, rcv_coor)
else:
    print("\nGörünür uydu sayisi 4'ten az olduğu için DOP hesabi yapilamaz!")