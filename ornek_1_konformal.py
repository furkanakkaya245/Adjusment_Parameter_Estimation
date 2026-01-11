import pandas as pd

# Veri tablosundaki değerleri listeler halinde tanımlama
# Nokta 8, 9 ve 10 eksik görünüyor, bu yüzden 7'den sonra 11 ile devam ediyoruz.
nokta = [1, 2, 3, 4, 5, 6, 7, 11, 12, 13, 14, 15, 16]
X1 = [0.000, -23.099, 1.210, -10.840, 0.477, -9.874, -4.330, None, None, None, None, None, None]
Y1 = [0.000, 82.940, 67.565, 17.849, 24.249, -88.881, 23.929, None, None, None, None, None, None]
Z1 = [0.000, -50.223, -50.015, -40.557, -45.190, -47.984, -44.290, None, None, None, None, None, None]
X2 = [86.500, 93.363, 110.858, 83.483, 96.126, 50.373, 91.561, 70.827, 74.001, 67.763, 73.600, 55.065, 70.481]
Y2 = [-25.703, 60.302, 38.300, -4.057, -1.612, -102.472, -0.395, 76.422, 76.411, -12.802, -8.354, -79.707, -73.410]
Z2 = [1.776, -43.477, -43.655, -37.091, -4.126, -49.645, -40.338, -150.108, -150.151, -154.747, -154.631, -158.200, -158.135]

# Veri Sözlüğü (Dictionary) oluşturma
data = {
    'Nokta': nokta,
    'X1, mm': X1,
    'Y1, mm': Y1,
    'Z1, mm': Z1,
    'X2, mm': X2,
    'Y2, mm': Y2,
    'Z2, mm': Z2
}

# Pandas DataFrame oluşturma
df = pd.DataFrame(data)

# DataFrame'i Excel dosyasına kaydetme
# 'index=False' parametresi, Excel'e ekstra bir satır numarası sütunu eklenmesini engeller.
dosya_adi = 'C:/Users/Fatih BLACK/Documents/HYTO/2.Sınıf/Fotogrametri-II/foto_kod/uc_b_konformal_donusumModel_Koordinatları.xlsx'
df.to_excel(dosya_adi, index=False)

print(f"Veriler başarıyla '{dosya_adi}' adlı Excel dosyasına aktarıldı.")