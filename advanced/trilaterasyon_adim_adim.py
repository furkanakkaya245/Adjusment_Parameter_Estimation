import numpy as np
import math
from paramDic_2 import Cr_, deltaCap_standart, xCap

def mesafe(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)

# SABİT NOKTALAR
C1x, C1y = -141.88, 87.12
C2x, C2y = 95.94, 106.65
C3x, C3y = 215.67, 79.42
C4x, C4y = -291.53, 19.61
C5x, C5y = -123.91, -128.95

# ÖLÇÜLER
L1 = 299.94
L2 = 75.21
L3 = 60.97
L4 = 450.64
L5 = 340.12

P1x = 156.87
P1y = 61.30

dC1P1 = mesafe(C1x, C1y, P1x, P1y)
dC2P1 = mesafe(C2x, C2y, P1x, P1y)
dC3P1 = mesafe(C3x, C3y, P1x, P1y)

# TÜREVLER (Design Matrix A için)
# Formül: (P_bilinmeyen - P_sabit) / Mesafe
# L1
a1_1 = (P1x - C1x) / dC1P1
a1_2 = (P1y - C1y) / dC1P1

# L2
a2_1 = (P1x - C2x) / dC2P1
a2_2 = (P1y - C2y) / dC2P1

# L3
a3_1 = (P1x - C3x) / dC3P1
a3_2 = (P1y - C3y) / dC3P1

A = np.array([
    [a1_1, a1_2],
    [a2_1, a2_2],
    [a3_1, a3_2]
])

W = np.array([
    [dC1P1 - L1],
    [dC2P1 - L2],
    [dC3P1 - L3]
])

sig_olcu = 0.03
Cr = Cr_(3, sig_olcu) 
x0_normal = np.array([[P1x], [P1y]])
deltaCap = deltaCap_standart(A, Cr, W)
xCap_sonuc = xCap(x0_normal, deltaCap)

print("--- A ŞIKKI (L1-L3) SONUCU ---")
print(f"deltaCap (Düzeltmeler):\n{deltaCap}")
print(f"xCap (Kesin Koordinatlar):\n{xCap_sonuc}")