import numpy as np
from paramDic_2 import KalmanFiltresi, Cr_
import matplotlib.pyplot as plt
# VERİ
t = np.array([0.0,10.0,20])
L_measures = np.array([
    [79.5,8.0],
    [160.5,8.1]   
])
# SABİT HIZ 
# Durum Vektörü: [x,y,vx,vy]
x_cap = np.array([[0], [7.9]])
Cx_cap = np.diag([1.0, 1.0])
# Cx_cap= np.linalg.inv(A.T@A) 
# delta_cap = x_cap
delta_cap = np.zeros((2, 1))
sig=1.00
Cr = Cr_(2,sig) # Ölçüm Gürültüsü
Ce = np.eye(2) * 1.0 # Sistem Gürültüsü 
A = np.array([[1, 0], 
              [0, 1]])
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
