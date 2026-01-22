import numpy as np
from paramDic_2 import KalmanFiltresi

# VERİ
t = np.array([0.00, 9.54, 13.11, 19.94])
L_measures = np.array([
    [-132.75, -314.42], 
    [-63.45, -203.74],  
    [28.33, -24.47]     
])


# SABİT HIZ 
# Durum Vektörü: [x, y, vx, vy]
x_cap = np.array([[-188.74], [-390.69], [6.67], [6.32]])
Cx_cap = np.diag([9.0, 9.0, 25.0, 25.0])
# delta_cap = x_cap
delta_cap = np.zeros((4, 1))
Cr = np.eye(2) * 9.0 # Ölçüm Gürültüsü
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

# SABİT İVME 
# Durum Vektörü: [x, y, vx, vy, ax, ay]
x_cap = np.array([[-188.74], [-390.69], [6.67], [6.32], [0.0], [0.0]])
Cx_cap = np.diag([9.0, 9.0, 25.0, 25.0, 100.0, 100.0])
delta_cap = np.zeros((6, 1))
Cr = np.eye(2) * 9.0   # Sadece konum ölçüyoruz (m=2)
Ce = np.eye(6) * 1.0   # 6 durum için sistem gürültüsü (n=6)
A = np.array([[1, 0, 0, 0, 0, 0], 
              [0, 1, 0, 0, 0, 0]])

# Çözüm: 
kf = KalmanFiltresi(model_tipi="sabit_ivme")
print("--- SABİT İVME MODELİ ÇÖZÜMÜ ---")
for i in range(1, len(t)):
    dt = t[i] - t[i-1]
    L_curr = L_measures[i-1].reshape(2, 1)
    x_cap, Cx_cap, delta_cap, G,W,S,Cx_Pred,x_pred,x_prev = kf.adim_hesapla( x_cap, Cx_cap, delta_cap, L_curr, dt, A, Cr, Ce )
    print(f"\nEVRE t{i} (t={t[i]} s):")
    print(f"ax, ay: {x_cap[4,0]:.4f}, {x_cap[5,0]:.4f}")
    print(f"[x, y, vx, vy]:\n{x_cap[:4]}")
    print(f"CxCap:\n{(Cx_cap)}")
    print(f"S:\n{S}")
    print("-" * 40)