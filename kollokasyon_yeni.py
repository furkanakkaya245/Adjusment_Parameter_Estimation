import numpy as np
import matplotlib.pyplot as plt
from paramDic_2 import Kollokasyon

# --- HASSASİYET AYARI ---
np.set_printoptions(precision=None, suppress=False, linewidth=200)

# 1. VERİ GİRİŞİ
x_val = [0, 1.445, 2.890, 4.335, 5.780]
l_val = [0.6108, 1.0863, 2.9034, 4.5925, 6.2714]

solver = Kollokasyon(x_val, l_val)

# Raporlama Fonksiyonu
def raporla(baslik, sonuc):
    print(f"\n{'='*60}")
    print(f"{baslik}")
    print(f"{'='*60}")
    
    keys = ["deltaCap", "xCap", "sCap", "rCap", "L", "N"]
    
    for k in keys:
        if k in sonuc:
            print(f"\n>>> {k}:")
            val = sonuc[k]
            if val.ndim == 2 and val.shape[1] == 1:
                print(val.flatten())
            else:
                print(val)
    print("-" * 70)

# =======================================================
# B ŞIKKI: KOLLOKASYON
# =======================================================
W_tahta = [0.0, 0.0000495, -1.341501, -2.5550515, -3.758402]
x0_tahta = [0.6108, 0.3291] 

print("Çözüm Başlatılıyor (Yuvarlama Yok)...")

# DÜZELTME: 'metod' parametresi SİLİNDİ
sonuc_B = solver.coz(
    C0=0.1260, 
    a=0.6, 
    sigma_noise=0.1, 
    custom_W=W_tahta,
    custom_x0=x0_tahta
)

raporla("B ŞIKKI SONUÇLARI (Saf Hassasiyet)", sonuc_B)

# =======================================================
# C ŞIKKI (a=1.0)
# =======================================================
# DÜZELTME: 'metod' parametresi SİLİNDİ
sonuc_C = solver.coz(
    C0=0.05, 
    a=1.0, 
    sigma_noise=0.1,
    custom_W=W_tahta,
    custom_x0=x0_tahta
)

raporla("C ŞIKKI SONUÇLARI", sonuc_C)

# GRAFİK
plt.figure(figsize=(10, 6))
plt.scatter(x_val, l_val, color='red', s=80, zorder=5, label='Ölçümler')
plt.plot(x_val, sonuc_B['y_total'], 'b-o', label='B (a=0.6)')
plt.plot(x_val, sonuc_C['y_total'], 'g-x', label='C (a=1.0)')
plt.plot(x_val, sonuc_B['y_trend'], 'k--', alpha=0.5, label='Trend')
plt.title("Kollokasyon Analizi (Yuvarlamasız)")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.show()