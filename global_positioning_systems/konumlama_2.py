from paramDic_2 import deltaCap_standart, Cr_, dms_to_radian, xCap
from paramDic_2 import GNSS_trilaterasyon as konumlama
from paramDic_2 import ecef_to_geodetic
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
        
        sonuclar[uydu_id] = {"Zenit": zenith, "Azimut": azimuth}
        print(f"{uydu_id} Zenit Açisi  : {zenith} derece")
        print(f"{uydu_id} Azimut Açisi : {azimuth} derece\n")
        
    return sonuclar

# Veriler
GIRS_coor= np.array([[3782947.6300],
                [2997054.3943],
                [4155987.9551]])
lat,lon,h=ecef_to_geodetic(GIRS_coor[0].item(),GIRS_coor[1].item(),GIRS_coor[2].item())
print(f"enlem: {lat}\nboylam: {lon}")
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
# Uydu Acilari  
R = R2enu(lat, lon)
uydu_acilari = tum_uydulari_hesapla(Sat_coor, GIRS_coor[0].item(),GIRS_coor[1].item(),GIRS_coor[2].item(), R)

# DOP Değerlerinin Hesaplanması
Rec_X = float(GIRS_coor[0].item())
Rec_Y = float(GIRS_coor[1].item())
Rec_Z = float(GIRS_coor[2].item())

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

# Konumlama
X1 = float(GIRS_coor[0].item())
Y1 = float(GIRS_coor[1].item())
Z1 = float(GIRS_coor[2].item())

A_list = []
W_list = []
uydu_sayisi = len(Sat_coor)

for i in range(uydu_sayisi):

    sx = float(Sat_coor[i][0].item())
    sy = float(Sat_coor[i][1].item())
    sz = float(Sat_coor[i][2].item())
    
    P_olculen = float(pseudoranges[i].item())
    
    uydu_hesap = konumlama(X1, Y1, Z1, sx, sy, sz)
    
    d_hesaplanan = uydu_hesap.d0()
    
    turevler = uydu_hesap.turev()
    ax = turevler[0]
    ay = turevler[1]
    az = turevler[2]
    
    A_list.append([ax, ay, az, 1])
    
    W_list.append([d_hesaplanan - P_olculen])

A = np.array(A_list)
W = np.array(W_list)
print(f"\nA={A}")
print(f"W={W}")

sig = 3
Cr = Cr_(uydu_sayisi, sig)
deltaCap = deltaCap_standart(A, Cr, W)
deltaX = deltaCap[0].item()
deltaY = deltaCap[1].item()
deltaZ = deltaCap[2].item()

xCap = X1 + deltaX
yCap = Y1 + deltaY
zCap = Z1 + deltaZ

print("\ndeltaCap :")
print(f"deltaX = {deltaX} m")
print(f"deltaY = {deltaY} m")
print(f"deltaZ = {deltaZ} m")

print("\nAlıcı_Konumu :")
print(f"x = {xCap} m")
print(f"y = {yCap} m")
print(f"z = {zCap} m")

