import numpy as np
import paramDic_2
from paramDic_2 import GNSS

print("--- GNSS İSTASYON VE UYDU ANALİZİ ---\n")

# 1. Alıcı Verileri ve Temiz 1D Dizi Tanımı
lat = 39.0
lon = 30.0
h = 1000.0
X, Y, Z = paramDic_2.geodetic_to_ecef(lat, lon, h)

recv_coor = np.array([X, Y, Z]) 

# 2. Uydu Koordinatları ve Sözde-Mesafeler (Temiz Dizi Tanımları)
Sat_coor = np.array([
    [ 15483704.907,  4291236.535,  19966556.765],
    [  6963767.996,  8910990.150,  21214948.604],
    [ 17144509.155, -9879352.949,  12468711.396],
    [ 10801779.303, 22664639.601,   -346547.608],
    [ 14981670.526, -13406040.750, 10725837.817],
    [ 19096453.795, 14302362.866,  12268186.638],
    [ 18981860.770, 14707284.339,  13490996.501],
    [ 14308626.738,  5615519.874,  19578204.448],
    [ 19135856.558, -5575633.645,  17154529.082],
    [ -7822806.434,  9989892.320,  17797054.899]
])

pseudoranges = np.array([
    19584066.939, 
    18944319.793, 
    19129197.155, 
    21643796.134, 
    20295500.251, 
    20675932.684, 
    21336692.926, 
    18785921.035, 
    21407584.406, 
    19845912.701  
])

# 3. UYDU AÇILARI VE YÜKSEKLİK (ALTITUDE) HESAPLAMALARI
uydu_acilari = GNSS.tum_uydulari_hesapla(Sat_coor, X, Y, Z)

# EKK'ya gidecek "sağlam" veriler için boş listeler
gecerli_uydular = []
gecerli_pseudoranges = []
kesme_acisi = 10.0 # 10 derecenin altındaki uyduları çöpe atacağız

print("\n--- UYDU UZAY YÜKSEKLİKLERİ VE GÖRÜNÜRLÜK DURUMU ---")
for i, sat in enumerate(Sat_coor):
    uydu_id = f"Uydu_{i+1}"
    
    # Uydu Yüksekliğini Bulma: ECEF -> Geodetic (Lat, Lon, H)
    s_lat, s_lon, s_h = paramDic_2.ecef_to_geodetic(sat[0], sat[1], sat[2])
    
    el = uydu_acilari[uydu_id]["Elevasyon"]
    az = uydu_acilari[uydu_id]["Azimut"]
    
    # s_h metredir. /1000 yaparak km'ye çevirip daha okunaklı basıyoruz.
    print(f"{uydu_id:<8} -> Yükseklik: {s_h/1000:9.3f} km | Elev: {el:6.2f}° | Azimut: {az:7.2f}°")
    
    # 4. GÜVENLİ FİLTRELEME (Uydu elenirse, ona ait ölçü de elenmek zorundadır!)
    if el >= kesme_acisi:
        gecerli_uydular.append(sat)
        gecerli_pseudoranges.append(pseudoranges[i])

# Listeleri matematiksel işlemler için tekrar Numpy dizisine çevir
gecerli_uydular = np.array(gecerli_uydular)
gecerli_pseudoranges = np.array(gecerli_pseudoranges)

print(f"\nToplam 10 uydudan {len(gecerli_uydular)} tanesi kesme açısını geçti ve dengelemeye alınıyor.")

# 5. DOP VE KABA KONUMLAMA (SADECE GEÇERLİ UYDULARLA)
if len(gecerli_uydular) >= 4:
    # DOP Hesabı
    GDOP, PDOP, HDOP, VDOP, TDOP = GNSS.ecef_to_DOP(gecerli_uydular, recv_coor)
    
    # Konumlama
    A, W, xCap, yCap, zCap, deltaX, deltaY, deltaZ = GNSS.kartezyen_konumlama(
        gecerli_uydular, 
        X, Y, Z, 
        gecerli_pseudoranges, # <- Artık filtrelenmiş veriyi gönderiyoruz
        sig=3
    )
else:
    print("\nKRİTİK UYARI: Yeterli uydu (Min 4) kalmadığı için konum kestirimi yapılamaz!")