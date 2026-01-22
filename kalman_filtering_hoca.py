import numpy as np
from paramDic_2 import KalmanFiltresi

# --- VERİ SETİ ---
t = np.array([0.00, 9.54, 13.11, 19.94])
L_measures = np.array([
    [-132.75, -314.42], 
    [-63.45, -203.74],  
    [28.33, -24.47]     
])

# BAŞLANGIÇ (Hoca Mantığı)
x_cap = np.array([[-188.74], [-390.69], [6.67], [6.32]])
Cx_cap = np.diag([9.0, 9.0, 25.0, 25.0])

# DİKKAT: Hoca delta_cap'i başlangıçta SIFIR alıyor ancak 
# x_cap'e ekleme yaparken önceki delta'yı kullanıyor.
delta_cap = np.zeros((4, 1)) 

Cr = np.eye(2) * 9.0 
Ce = np.eye(4) * 1.0 
A = np.array([[1, 0, 0, 0], [0, 1, 0, 0]])

kf = KalmanFiltresi(model_tipi="sabit_hiz")

print("--- HOCANIN ADIMLARINA TAM UYUMLU ÇÖZÜM ---")

for i in range(1, len(t)):
    dt = t[i] - t[i-1]
    
    # HOCANIN VERİ EŞLEŞTİRMESİ (image.png'den teyitli)
    # Hoca t3 (19.94s) anında L2'yi ([-63.45, -203.74]) kullanıyor.
    if i == 1: L_curr = L_measures[0].reshape(2, 1) # t1 -> L1
    elif i == 2: L_curr = L_measures[0].reshape(2, 1) # t2 -> L1
    elif i == 3: L_curr = L_measures[1].reshape(2, 1) # t3 -> L2

    # MATEMATİKSEL MOTORU ÇALIŞTIR
    # Sınıfın döndürdüğü değerleri hocanın isimlendirmesiyle alıyoruz
    x_cap, Cx_cap, delta_cap, G, W, S, Cx_P, x_p, x_prev = kf.adim_hesapla(
        x_cap, Cx_cap, delta_cap, L_curr, dt, A, Cr, Ce
    )

    if i == 3:
        # Hocanın ekranındaki x3p = [187.22, 268.98...] değerini yakalayıp yakalamadığını kontrol et
        print(f"EVRE t3 Tahmin (x3p):\n{x_p.flatten()}") 
        print(f"Hocanın xCap3 Sonucu:\n[256.204, 383.276, 44.407, 79.502]")
        print(f"Senin xCap3 Sonucun:\n{x_cap.flatten()}")