import numpy as np
import math
from paramDic_2 import dms_to_radian, deltaCap_standart, xCap

def semt_rad(x1, y1, x2, y2):
    return math.atan2(y2 - y1, x2 - x1)

class TriangulasyonAciGradyan:
    def __init__(self, x1, y1, x2, y2):
        self.Dx = x2 - x1
        self.Dy = y2 - y1
        self.Payda = self.Dx**2 + self.Dy**2
        self.S_kare = self.Payda
        
    def gradyan_hesapla(self):
        dx1 = -self.Dy / self.S_kare 
        dy1 = self.Dx / self.S_kare 
        dx2 = self.Dy / self.S_kare 
        dy2 = -self.Dx / self.S_kare 
        return dx1, dy1, dx2, dy2

C1x = 21.94
C1y = 45.88
C2x = -13.11
C2y = -0.39

L_rad_vector = np.array([
    dms_to_radian(42.03069, 0, 0),
    dms_to_radian(66.07014, 0, 0),
    dms_to_radian(71.89783, 0, 0)
])

P = np.eye(3)

X0 = np.array([61.02, -26.27])
x0, y0 = X0[0], X0[1]

t_P1C1 = TriangulasyonAciGradyan(x0, y0, C1x, C1y).gradyan_hesapla() 
t_P1C2 = TriangulasyonAciGradyan(x0, y0, C2x, C2y).gradyan_hesapla() 
t_C2P1 = TriangulasyonAciGradyan(C2x, C2y, x0, y0).gradyan_hesapla()
t_C1P1 = TriangulasyonAciGradyan(C1x, C1y, x0, y0).gradyan_hesapla()

dL1x = t_P1C2[0] - t_P1C1[0]
dL1y = t_P1C2[1] - t_P1C1[1]

dL2x = -t_C2P1[2]
dL2y = -t_C2P1[3]

dL3x = t_C1P1[2]
dL3y = t_C1P1[3]

A = np.array([
    [dL1x, dL1y],
    [dL2x, dL2y],
    [dL3x, dL3y]
])

F1 = semt_rad(x0, y0, C2x, C2y) - semt_rad(x0, y0, C1x, C1y)
F2 = semt_rad(C2x, C2y, C1x, C1y) - semt_rad(C2x, C2y, x0, y0)
F3 = semt_rad(C1x, C1y, x0, y0) - semt_rad(C1x, C1y, C2x, C2y)

F_vector = np.array([F1, F2, F3])

W = np.arctan2(np.sin(F_vector - L_rad_vector), np.cos(F_vector - L_rad_vector))
W = W.reshape(-1, 1)

delta_cap = deltaCap_standart(A, P, W)

X_cap = xCap(X0.reshape(-1, 1), delta_cap)

print("A Matrisi:\n", A)
print("\nW Vektörü:\n", W)
print("\nDelta (Düzeltme):\n", delta_cap)
print("\nKesin Koordinatlar (X, Y):")
print(f"{X_cap[0][0]:.4f}")
print(f"{X_cap[1][0]:.4f}")