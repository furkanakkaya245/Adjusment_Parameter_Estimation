import numpy as np
import matplotlib.pyplot as plt
from paramDic_2 import Kollokasyon, Prediksiyon

# Hassasiyet
np.set_printoptions(precision=None, suppress=False, linewidth=200)

# Veriler ve Hocanın Sabitleri
x_val = [0, 1.445, 2.890, 4.335, 5.780]
l_val = [0.6108, 1.0863, 2.9034, 4.5925, 6.2714]
W_tahta = [0.0, 0.0000495, -1.341501, -2.5550515, -3.758402]
x0_tahta = [0.6108, 0.3291] 

# 1. MODELİ KUR VE ÇÖZ
solver = Kollokasyon(x_val, l_val)

# Parametreler (Bunları Prediksiyon'a da elle vereceğiz)
C0_val = 0.1260
a_val = 0.6

sonuc_model = solver.coz(
    metod="kollokasyon", 
    C0=C0_val, a=a_val, sigma_noise=0.1, 
    custom_W=W_tahta, custom_x0=x0_tahta
)

print(">>> Model Çözüldü. sCap (s):")
print(sonuc_model["sCap"].flatten())

# 2. PREDIKSIYON (KESTİRİM)
# Sınıfı başlatırken solver'ı, sonucu ve parametreleri veriyoruz
predictor = Prediksiyon(solver, sonuc_model, C0_val, a_val)

# Ara Noktalar
x_ara = [(x_val[i] + x_val[i+1])/2 for i in range(len(x_val)-1)]
sonuc_tahmin = predictor.tahmin_et(x_ara)

print("\n>>> PREDIKSIYON SONUÇLARI (Ara Noktalar):")
print(f"SpCap: {sonuc_tahmin['SpCap'].flatten()}")
print(f"Total: {sonuc_tahmin['Total_p'].flatten()}")

print("\n>>> z VEKTÖRÜ [Sp / s]:")
print(sonuc_tahmin["z_vector"].flatten())

# 3. GRAFİK (Pürüzsüz Eğri)
x_smooth = np.linspace(0, 6, 100)
grafik_tahmin = predictor.tahmin_et(x_smooth)

plt.figure(figsize=(10, 6))
plt.scatter(x_val, l_val, color='red', s=100, zorder=5, label='Ölçülen')
plt.scatter(x_val, sonuc_model['y_total'], color='blue', marker='x', s=80, label='Model (x)')
plt.scatter(x_ara, sonuc_tahmin["Total_p"], color='green', marker='s', s=80, label='Prediksiyon')
plt.plot(x_smooth, grafik_tahmin["Total_p"], 'k-', alpha=0.6, label='Eğri')
plt.legend()
plt.grid(True, linestyle=':')
plt.show()