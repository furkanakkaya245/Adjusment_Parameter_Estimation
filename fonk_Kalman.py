import numpy as np
from paramDic_2 import KalmanFiltresi

# --- 1. VERİ SETİ (Görseldeki Değerler) ---
t = np.array([0.00, 9.54, 13.11, 19.94])
# Ölçümler (L): Sadece x ve y konumları ölçülüyor
L_measures = np.array([
    [-132.75, -314.42], 
    [-63.45, -203.74],  
    [28.33, -24.47]     
])

# --- 2. BAŞLANGIÇ (t0) - SABİT İVME (6 DURUMLU) ---
# Durum: [x, y, vx, vy, ax, ay]
x_cap = np.array([[-188.74], [-390.69], [6.67], [6.32], [0.0], [0.0]])
# İvme (ax, ay) başlangıçta bilinmediği için varyansını yüksek (100) tutuyoruz
Cx_cap = np.diag([9.0, 9.0, 25.0, 25.0, 100.0, 100.0])
delta_cap = np.zeros((6, 1))

# Gürültüler
Cr = np.eye(2) * 9.0  # Sadece 2 konum ölçümü var
Ce = np.eye(6) * 1.0  # 6 durum için sistem gürültüsü

# --- 3. MODEL TANIMI ---
kf = KalmanFiltresi(model_tipi="sabit_ivme")

print(f"--- BAŞLANGIÇ (t0) ---\n{x_cap.flatten()}\n" + "="*40)

# --- 4. DÖNGÜ ---
for i in range(1, len(t)):
    dt = t[i] - t[i-1]
    
    # HATA DÜZELTME: Değişken adını L_curr olarak netleştirdik
    L_curr = L_measures[i-1].reshape(2, 1)
    
    # Sınıf içindeki matris boyutları n=6 olduğu için otomatik ayarlanacak
    kf = KalmanFiltresi(model_tipi="sabit_hiz")
    x_cap, Cx_cap, delta_cap, G = kf.adim_hesapla(x_cap, Cx_cap, delta_cap, L_curr, dt, Cr, Ce)
    
    print(f"EVRE t{i} (dt={dt:.2f}s):")
    print(f"Kestirilen İvmeler (ax, ay): {x_cap[4,0]:.4f}, {x_cap[5,0]:.4f}")
    print(f"deltaCap (Düzeltmeler):\n{delta_cap}")
    print(f"Yeni Belirsizlik (CxCap Diag):\n{(Cx_cap)}")
    print("-" * 40)