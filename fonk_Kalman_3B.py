import numpy as np
from paramDic_2 import KalmanFiltresi

# VERİ
t = np.array([0.00, 9.54, 13.11, 19.94])
L_measures = np.array([
    [-132.75, -314.42], 
    [-63.45, -203.74],  
    [28.33, -24.47]     
])

x_cap = np.array([[-188.74], [-390.69], [6.67], [6.32]])
Cx_cap = np.diag([9.0, 9.0, 25.0, 25.0])
delta_cap = np.zeros((4, 1))

Cr = np.eye(2) * 9.0 # Ölçüm Gürültüsü
Ce = np.eye(4) * 1.0 # Sistem Gürültüsü 
I = np.eye(2)   # Birim Matris
A = np.array([[1, 0, 0, 0], # Ölçüm Matrisi
              [0, 1, 0, 0]])

print(f"--- BAŞLANGIÇ (t0) ---")
print(f"Başlangiç Durumu (x, y, vx, vy):\n{x_cap.flatten()}\n" + "="*40)

# --- 4. ARDIŞIK ÇÖZÜM DÖNGÜSÜ ---
for i in range(1, len(t)):
    dt = t[i] - t[i-1]
    
    # Sabit Hız Model S Matrisi (4x4)
    # x = x0 + vx*dt | y = y0 + vy*dt
    S = np.array([[1, 0, dt, 0],
                  [0, 1, 0, dt],
                  [0, 0, 1, 0],
                  [0, 0, 0, 1]])
    
    L_curr = L_measures[i-1].reshape(2, 1)
    
    # KÜTÜPHANENDEN ÇAĞRILAN FONKSİYON
    kf = KalmanFiltresi(model_tipi="sabit_hiz")
    x_cap, Cx_cap, delta_cap, G = kf.adim_hesapla(x_cap, Cx_cap, delta_cap, L_curr, dt, Cr, Ce)
    
    # --- SONUÇLARI YAZDIRMA ---
    print(f"EVRE t{i} (t={t[i]} s):")
    print(f"Kalman Kazancı (G):\n{G}")
    print(f"Düzeltme Miktarı (deltaCap):\n{delta_cap}")
    print(f"Güncellenmiş Durum (xCap):\n{x_cap}")
    print(f"Yeni Belirsizlik (CxCap):\n{(Cx_cap)}")
    print("-" * 40)