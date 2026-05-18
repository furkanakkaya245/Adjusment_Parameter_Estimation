import numpy as np
import math
from paramDic_2 import geodetic_to_ecef

print("--- SINAV SORUSU ÇÖZÜMÜ: UYDU ECEF KOORDİNATLARI ---\n")

# 1. ABCD İstasyon Verileri
lat = 40.0000
lon = 40.0000
h = 1000.000

# İstasyon ECEF Koordinatlarının Hesaplanması
Xr, Yr, Zr = geodetic_to_ecef(lat, lon, h)
istasyon_ecef = np.array([[Xr], [Yr], [Zr]])

print(f"İstasyon ECEF (X, Y, Z): {Xr:.3f}, {Yr:.3f}, {Zr:.3f}\n")

# 2. İstasyonun ENU Rotasyon Matrisi (R_enu)
lat_rad = math.radians(lat)
lon_rad = math.radians(lon)

R_enu = np.array([
    [-math.sin(lon_rad), math.cos(lon_rad), 0],
    [-math.sin(lat_rad) * math.cos(lon_rad), -math.sin(lat_rad) * math.sin(lon_rad), math.cos(lat_rad)],
    [math.cos(lat_rad) * math.cos(lon_rad), math.cos(lat_rad) * math.sin(lon_rad), math.sin(lat_rad)]
])

# ENU'dan ECEF'e geçiş için matrisin tersi (Ortogonal matrislerde ters = transpoze)
R_enu_inv = R_enu.T

# 3. Uydu Verileri (PRN, Mesafe(m), Azimut(°), Elevasyon(°))
uydular = [
    ["G01", 20964271.916, 226.000, 24.000],
    ["G04", 19904076.867, 172.000, 52.000],
    ["G05", 19538509.901, 298.000, 51.000],
    ["G08", 19848983.494, 289.000, 55.000],
    ["G12", 20420434.156, 196.000, 49.000],
    ["G14", 20683762.551, 147.000, 77.000],
    ["G15", 21033592.953, 282.000, 21.000],
    ["G16", 20101432.953, 316.000, 23.000],
    ["G17", 18765065.661, 293.000, 53.000],
    ["G18", 21055608.007,  34.000, 74.000]
]

# 4. Her bir uydu için hesaplama
print(f"{'PRN':<5} | {'X_ecef (m)':<15} | {'Y_ecef (m)':<15} | {'Z_ecef (m)':<15}")
print("-" * 55)

for uydu in uydular:
    prn = uydu[0]
    S = uydu[1]
    az_rad = math.radians(uydu[2])
    el_rad = math.radians(uydu[3])
    
    # Kutupsaldan Yerel Kartezyene (East, North, Up)
    E = S * math.cos(el_rad) * math.sin(az_rad)
    N = S * math.cos(el_rad) * math.cos(az_rad)
    U = S * math.sin(el_rad)
    enu_vektoru = np.array([[E], [N], [U]])
    
    # Yerelden Global Uzaya Vektör Çevrimi (dX, dY, dZ)
    delta_ecef = R_enu_inv @ enu_vektoru
    
    # İstasyon koordinatlarına farkların eklenmesi
    uydu_ecef = istasyon_ecef + delta_ecef
    
    Xs = float(uydu_ecef[0][0])
    Ys = float(uydu_ecef[1][0])
    Zs = float(uydu_ecef[2][0])
    
    print(f"{prn:<5} | {Xs:>15.3f} | {Ys:>15.3f} | {Zs:>15.3f}")

print("-" * 55)