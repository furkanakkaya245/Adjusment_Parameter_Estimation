import numpy as np
from paramDic_2 import KalmanFiltresi

# HASSASİYET AYARI
np.set_printoptions(precision=4, suppress=True, linewidth=200)

t = np.array([0.0, 10.0, 20.0])

L_measures = np.array([
    [79.5, 8.0], 
    [160.5, 8.1]     
])


x_cap = np.array([[0.0], 
                  [7.9]])


Cx_cap = np.diag([1.0**2, 1.0**2])

# Düzeltme Vektörü (delta_cap)
delta_cap = np.zeros((2, 1))

# Matrisler
Cr = np.eye(2) * 1.0  # Ölçüm Gürültüsü (sig=1)
Ce = np.eye(2) * 1.0  # Sistem Gürültüsü (I birim matris verilmişti)

# Ölçüm Matrisi (A)
# Hem konumu hem hızı ölçtüğümüz için Birim Matris
A = np.eye(2)


kf = KalmanFiltresi(model_tipi="sabit_hiz")

print("--- SABİT HIZ MODELİ ÇÖZÜMÜ (SLAYT SORUSU) ---")
print(f"Başlangıç Durumu (t=0):\nKonum: {x_cap[0,0]}, Hız: {x_cap[1,0]}\n" + "="*60)

for i in range(1, len(t)):
    # Zaman farkı (dt)
    dt = t[i] - t[i-1]
    
    # Mevcut ölçüm vektörü (L)
    L_curr = L_measures[i-1].reshape(2, 1)
    
    x_cap, Cx_cap, delta_cap, G, W, S, Cx_Pred, x_pred, x_prev = kf.adim_hesapla(
        x_cap, Cx_cap, delta_cap, L_curr, dt, A, Cr, Ce
    )
    
    
    print(f"EVRE t{i} (t={t[i]} s):")
    print(f"Lcurr (Ölçüm):\n{L_curr.flatten()}")
    print(f"x_pred (Tahmin):\n{x_pred.flatten()}")
    print(f"G (Kazanç):\n{G}")
    print(f"xCap (Güncellenmiş):\n{x_cap.flatten()}")
    print(f"CxCap (Kovaryans):\n{Cx_cap}")
    print(f"S (Geçiş):\n{S}")
    print("-" * 60)