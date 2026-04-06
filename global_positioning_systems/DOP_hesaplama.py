<<<<<<< HEAD
print("a")
=======
import numpy as np
from paramDic_2 import GNSS_DOP

cozum = GNSS_DOP(lat_deg=39.887, lon_deg=32.758, h_meters=800)
print(f"Alici ECEF Koordinatlari:")
print(f"X: {cozum.X}, Y: {cozum.Y}, Z: {cozum.Z}\n")
cozum.uydu_ekle(prn=1,  az_deg=197, el_deg=35)
cozum.uydu_ekle(prn=3,  az_deg=45,  el_deg=20)
cozum.uydu_ekle(prn=8,  az_deg=133, el_deg=89)
cozum.uydu_ekle(prn=9,  az_deg=296, el_deg=70)
cozum.uydu_ekle(prn=13, az_deg=348, el_deg=40)

A_ecef = cozum.A()
print("ECEF Tasarim Matrisi (A):")
print(A_ecef)
dops = cozum.hesapla_dop()
print("DOP Değerleri:")
for key, value in dops.items():
    print(f"{key}: {value}")

    
>>>>>>> 4f4f387d60439d701ccfff6d89b3d6d390827b80