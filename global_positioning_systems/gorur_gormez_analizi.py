from paramDic_2 import deltaCap_standart, Cr_, dms_to_radian, xCap
from paramDic_2 import GNSS_trilaterasyon as konumlama
from paramDic_2 import geodetic_to_ecef
import numpy as np
from numpy.linalg import inv
import math

def R2enu(phi1,lam1):
    phi=dms_to_radian(phi1,0,0)
    lam=dms_to_radian(lam1,0,0)
    return np.array([[-np.sin(phi)*np.cos(lam), -np.sin(phi)*np.sin(lam), np.cos(phi)],
                     [-np.sin(lam), np.cos(lam), 0],
                     [np.cos(phi)*np.cos(lam), np.cos(phi)*np.sin(lam),np.sin(phi)]])
def calculate_satellite_angles(konum):
    E = float(konum[0].item())
    N = float(konum[1].item())
    U = float(konum[2].item())
    elevation_rad = np.arctan2(U, (E**2 + N**2)**0.5)
    elev_deg= np.degrees(elevation_rad)
    # zenith_deg = 90.0 - elev_deg
    azimuth_rad = np.arctan2(E , N)
    azimuth_deg = np.degrees(azimuth_rad) % 360.0
    # % 360.0 for azimut
    return elev_deg, azimuth_deg
def tum_uydulari_hesapla(sat_array, alici_x, alici_y, alici_z, R_matrisi):
    sonuclar = {} 
    print("Sat Angles (azimut/elevation):\n")
    j=0
    gorunen_uydu=[]
    for i, uydu_koor in enumerate(sat_array):
        uydu_id = f"Uydu_{i+1}" 
        ux = float(uydu_koor[0].item())
        uy = float(uydu_koor[1].item())
        uz = float(uydu_koor[2].item())
        
        Dx = ux - alici_x
        Dy = uy - alici_y
        Dz = uz - alici_z
        enu = R_matrisi @ np.array([[Dx], [Dy], [Dz]])
        zenith, azimuth = calculate_satellite_angles(enu)
        
        if (zenith > 0):
            j=j+1
            print(f"Gorunen Uydu Numarası : {uydu_id}")
            gorunen_uydu.append(uydu_id)
        
        sonuclar[uydu_id] = {"Zenit": zenith, "Azimut": azimuth}
        print(f"{uydu_id} Elevetion Açisi  : {zenith} derece")
        print(f"{uydu_id} Azimut Açisi : {azimuth} derece\n")
    print(f"Gorunen Uydu Sayisi : {j}\n Uydular : {gorunen_uydu}")
    return sonuclar

ANK_angle=np.array([[40],
                    [33]])

R = R2enu(ANK_angle[0].item(), ANK_angle[1].item())
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
# elev pozitif olanlar görür diğerleri istasyonu görmez
uydu_acilari = tum_uydulari_hesapla(Sat_coor, x,y,z, R)

sat_poz=np.array([[[23553858.9652], [ 10696530.3354 ], [-6556890.7665]],
                  [[-12985686.5465],[  19287151.5279 ],[ 12491300.1659]],
                  [[14221911.4840], [-7090656.1957 ], [21076904.7080]],
                  [ [14218238.4720],  [19512255.0996 ], [-11670952.0798]],
                  [[22474726.6767],  [4701888.0401 ], [13296320.8112]],
                  [[25204330.9684 ], [-5711889.7559 ],[ -7250385.1216]]])

# DOP DEGER HESAPLAMA
Rec_X = x
Rec_Y = y
Rec_Z = z

A_list = []

for sat in Sat_coor:
    sx = float(sat[0].item())
    sy = float(sat[1].item())
    sz = float(sat[2].item())
    dx = sx - Rec_X
    dy = sy - Rec_Y
    dz = sz - Rec_Z
    rho = math.sqrt(dx**2 + dy**2 + dz**2)
    ax = -dx / rho
    ay = -dy / rho
    az = -dz / rho
    A_list.append([ax, ay, az, 1])

A = np.array(A_list)
Q = inv(A.T @ A)
Q_xyz = Q[:3, :3]
Q_enu = R @ Q_xyz @ R.T
GDOP = math.sqrt(np.trace(Q))               
PDOP = math.sqrt(np.trace(Q_xyz))           
HDOP = math.sqrt(Q_enu[0, 0] + Q_enu[1, 1]) 
VDOP = math.sqrt(Q_enu[2, 2])               
TDOP = math.sqrt(Q[3, 3])                  

print(f"\nDOP Değerleri")
print(f"GDOP : {GDOP}")
print(f"PDOP : {PDOP}")
print(f"HDOP : {HDOP}")
print(f"VDOP : {VDOP}")
print(f"TDOP : {TDOP}")



