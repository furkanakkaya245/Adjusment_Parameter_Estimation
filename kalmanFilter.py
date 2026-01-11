import numpy as np
from paramDic_2 import KalmanFiltresi
# Veri
t = np.array([0.0, 10.0, 20.0])
x = np.array([0.0, 79.5, 160.5])
v = np.array([7.9, 8.0, 8.1])

x_cap = np.array([[x[0]], [v[0]]]) 
Cx_cap = np.eye(2) 
delta_cap = np.zeros((2, 1))

A = np.eye(2)   
Cr = np.eye(2)  # Ölçüm gürültüsü
Ce = np.eye(2)  # Sistem gürültüsü


kf = KalmanFiltresi(model_tipi="sabit_hiz")
print("--- SABİT HIZ MODELİ ÇÖZÜMÜ ---")
print(f"--- BAŞLANGIÇ (t=0) ---\nxCap:\n{x_cap}\n" + "="*35)
for i in range(1, len(t)):
    dt = t[i] - t[i-1]
    L_curr = np.array([[x[i]], [v[i]]])
    x_cap, Cx_cap, delta_cap, G = kf.adim_hesapla(
        x_cap, Cx_cap, delta_cap, L_curr, dt, A, Cr, Ce
    )
    
    print(f"--- EVRE t{i} (t={t[i]} s) ---")
    print(f"G:\n{G}")
    print(f"deltaCap:\n{delta_cap}")
    print(f"xCap:\n{x_cap}")
    print(f"CxCap:\n{Cx_cap}")
    print("-" * 35)