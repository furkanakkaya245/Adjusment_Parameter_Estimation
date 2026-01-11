import numpy as np
import math
from numpy.linalg import inv
# 'paramDic_2' dosyasından gerekli fonksiyonları varsayılan olarak içe aktarıyoruz
# from paramDic_2 import dms_to_radian, TriangulasyonAciGradyan

# --- Harici Fonksiyonların Basitleştirilmiş Tanımları (Senin dosyanı taklit eder) ---

def dms_to_radian(derece, dakika, saniye):
    """Derece, Dakika, Saniye'yi Radyana çevirir."""
    decimal_degree = derece + dakika / 60 + saniye / 3600
    return math.radians(decimal_degree)

def semt_rad(x1, y1, x2, y2):
    """Semti radyan cinsinden döndürür: atan2(dy, dx)"""
    return math.atan2(y2 - y1, x2 - x1)

def N_standart(A, P):
    """Normal Matris N = A.T @ P @ A hesaplar."""
    return A.T @ P @ A

def deltaCap_standart(A, P, W):
    """Bilinmeyen düzeltme vektörü delta_cap = (N^-1) @ U hesaplar."""
    N = N_standart(A, P)
    U = A.T @ P @ W
    return inv(N) @ U

def xCap(x0, deltaCap):
    """Düzeltilmiş koordinatları hesaplar: X_cap = X0 + delta_cap."""
    return x0 + deltaCap

# Lütfen TriangulasyonAciGradyan class'ının matematiksel olarak doğru olduğundan emin ol.
# Örnek tanım (Hata yapmamak için önceki yanıttaki doğru versiyonu kullanıyorum)
class TriangulasyonAciGradyan:
    def __init__(self, x1, y1, x2, y2):
        self.Dx = x2 - x1
        self.Dy = y2 - y1
        self.Payda = self.Dx**2 + self.Dy**2
        if self.Payda == 0:
            raise ValueError("Noktalar çakışıyor! Payda sıfır olamaz.")
        self.S_kare = self.Payda
        
    def gradyan_hesapla(self):
        dx1 = -self.Dy / self.S_kare 
        dy1 = self.Dx / self.S_kare 
        dx2 = self.Dy / self.S_kare 
        dy2 = -self.Dx / self.S_kare 
        return dx1, dy1, dx2, dy2

# -----------------------------------------------------------------

# Nirengi Ağı
# Tanımlamalar (Sabit Koordinatlar)
C1x = 21.94
C1y = 45.88
C2x = -13.11
C2y = -0.39

# Ölçüler (L_i)
L1_rad = dms_to_radian(42, 3, 0.69) # 42.03069 derece
L2_rad = dms_to_radian(66, 4, 1.4)  # 66.07014 derece
L3_rad = dms_to_radian(71, 53, 52.18) # 71.89783 derece
# NOT: Senin dms_to_radian fonksiyonunun ondalık dereceyi direkt derece, dakika, saniye olarak mı beklediğini netleştirdim.
# Orjinal sorunda derece 42.03069 şeklinde ondalık olarak verilmişti. Burada DAKIKA ve SANİYE sıfır kabul edilmiştir.
# Düzeltme: Eğer fonksiyonun derece, dakika, saniye bekliyorsa L1=42.03069, 0, 0 şeklinde olmalıdır.
# Kullanım kolaylığı için ondalık dereceyi doğrudan radyana çeviriyorum.

L_rad_vector = np.array([
    dms_to_radian(42.03069, 0, 0),
    dms_to_radian(66.07014, 0, 0),
    dms_to_radian(71.89783, 0, 0)
])

# Hassasiyet
sig = dms_to_radian(0, 0, 2)
# Ağırlık Matrisi P = I (Tüm hatalar eşit olduğundan)
P = np.eye(3) 

# Yaklaşık Noktalar
X0 = np.array([61.02, -26.27])
x0, y0 = X0[0], X0[1]

# --- 1. A Matrisinin (Jakobiyen) Hesaplanması (Senin Kod Bloğun) ---

t_P1C1 = TriangulasyonAciGradyan(x0, y0, C1x, C1y).gradyan_hesapla() 
t_P1C2 = TriangulasyonAciGradyan(x0, y0, C2x, C2y).gradyan_hesapla() 
t_C2P1 = TriangulasyonAciGradyan(C2x, C2y, x0, y0).gradyan_hesapla()
t_C1P1 = TriangulasyonAciGradyan(C1x, C1y, x0, y0).gradyan_hesapla()

# A1 (L1): F1 = a_P1C2 - a_P1C1. (dx1, dy1 kullanılır)
dL1x = t_P1C2[0] - t_P1C1[0]
dL1y = t_P1C2[1] - t_P1C1[1]

# A2 (L2): F2 = a_C2C1 - a_C2P1. (P1=x2,y2). Türevler: -[dx2, dy2]
dL2x = -t_C2P1[2]
dL2y = -t_C2P1[3]

# A3 (L3): F3 = a_C1P1 - a_C1C2. (P1=x2,y2). Türevler: +[dx2, dy2]
dL3x = t_C1P1[2]
dL3y = t_C1P1[3]

A = np.array([
    [dL1x, dL1y],
    [dL2x, dL2y],
    [dL3x, dL3y]
])

# --- 2. W Matrisinin (Serbest Terimler) Hesaplanması (W = F(X0) - L) ---

F1 = semt_rad(x0, y0, C2x, C2y) - semt_rad(x0, y0, C1x, C1y)
F2 = semt_rad(C2x, C2y, C1x, C1y) - semt_rad(C2x, C2y, x0, y0)
F3 = semt_rad(C1x, C1y, x0, y0) - semt_rad(C1x, C1y, C2x, C2y)

F_vector = np.array([F1, F2, F3])

# Normalize etme (Açı farkları 2*pi'yi aşabilir, ancak W için farkın kendisi önemlidir.)
# W = F - L
W = F_vector - L_rad_vector
W = W.reshape(-1, 1) # Vektör matrisine çevir

# --- 3. EKK Çözümü ---

# Düzeltme Vektörü delta_cap
delta_cap = deltaCap_standart(A, P, W)

# Düzeltilmiş Koordinatlar
X_cap = xCap(X0.reshape(-1, 1), delta_cap)

# --- SONUÇLARIN GÖSTERİLMESİ ---

print("--- EKK Nirengi Çözümü (1. İterasyon) ---")
print("Jakobiyen Matrisi (A):\n", A.round(5))
print("\nSerbest Terim Vektörü (W) (Radyan):\n", W.round(5))
print("\nDüzeltme Vektörü (dX, dY):\n", delta_cap.round(4))
print("\n--- Nihai Koordinatlar ---")
print(f"X_P1: {X_cap[0][0]:.4f} m")
print(f"Y_P1: {X_cap[1][0]:.4f} m")