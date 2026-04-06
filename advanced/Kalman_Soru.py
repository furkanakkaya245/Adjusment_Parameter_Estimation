import numpy as np
from paramDic_2 import KalmanFiltresi, Cr_
import matplotlib.pyplot as plt
# VERİ
t = np.array([0.0,9.21,16.47,22.91,30.72])
L_measures = np.array([
    [88.24,141.97],  
    [125.30,200.97],
    [158.82,251.42],
    [192.77,312.90]     
])
# SABİT HIZ 
# Durum Vektörü: [x,y,vx,vy]
x_cap = np.array([[44.89], [71.42], [5.52], [7.75]])
Cx_cap = np.diag([9.0, 9.0, 1.0, 1.0])
# Cx_cap= np.linalg.inv(A.T@A) 
# delta_cap = x_cap
delta_cap = np.zeros((4, 1))
sig=3
Cr = Cr_(2,sig) # Ölçüm Gürültüsü
Ce = np.eye(4) * 1.0 # Sistem Gürültüsü 
A = np.array([[1, 0, 0, 0], 
              [0, 1, 0, 0]])
# Çözüm: 
kf = KalmanFiltresi(model_tipi="sabit_hiz")
print("--- SABİT HIZ MODELİ ÇÖZÜMÜ ---")
print(f"Başlangiç Durumu (x, y, vx, vy):\n{x_cap.flatten()}\n" + "="*40)
for i in range(1, len(t)):
    dt = t[i] - t[i-1]
    L_curr = L_measures[i-1].reshape(2, 1) 
    # HATA BURADAYDI: A parametresini ekledik (Cr ve Ce'den önce)
    x_cap, Cx_cap, delta_cap, G,W,S,Cx_Pred,x_pred,x_prev = kf.adim_hesapla(x_cap, Cx_cap, delta_cap, L_curr, dt, A, Cr, Ce)
    print(f"EVRE t{i} (t={t[i]} s):")
    print(f"G:\n{G}")
    print(f"deltaCap:\n{delta_cap}")
    print(f"xCap:\n{x_cap}")
    print(f"x_pred:\n{x_pred}")
    print(f"x_prev:\n{x_prev}")
    print(f"CxCap:\n{(Cx_cap)}")
    print(f"CxPred:\n{(Cx_Pred)}")
    print(f"W:\n{W}")
    print(f"S:\n{S}")
    print(f"Lcurr:\n{L_curr}")
    print("-" * 40)

# ==========================================
t_values = np.array([0.0, 9.54, 13.11, 19.94])
# Kestirilen Konumlar (xCap sonuçları - Mavi Çizgi)
x_est = np.array([-188.74, -132.72, -76.34, 33.73])
y_est = np.array([-390.69, -314.48, -216.99, -19.37])
# Ölçülen Konumlar (L_measures - Kırmızı Çarpı)
x_meas = np.array([-132.75, -63.45, 28.33])
y_meas = np.array([-314.42, -203.74, -24.47])
plt.figure(figsize=(10, 8))
plt.plot(x_est, y_est, 'b-o', label='Kalman Filtresi (Sabit Hız)', linewidth=2, markersize=8)
plt.scatter(x_meas, y_meas, color='red', marker='x', s=100, label='Ölçümler (GNSS)', zorder=5)
for i in range(len(t_values)):
    plt.text(x_est[i], y_est[i]+10, f't{i}', fontsize=12, color='blue', ha='center', fontweight='bold')
    if i > 0:
        dt = t_values[i] - t_values[i-1]
        mid_x = (x_est[i] + x_est[i-1]) / 2
        mid_y = (x_est[i] + y_est[i-1]) / 2
        plt.text(mid_x, mid_y-15, f'dt = {dt:.2f}s', fontsize=10, color='green', ha='right', fontweight='bold')
plt.title("Kalman Filtresi Yörünge Analizi (Sabit Hız)", fontsize=14)
plt.xlabel("X Konumu (m)")
plt.ylabel("Y Konumu (m)")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)
plt.axis('equal') 
plt.show()