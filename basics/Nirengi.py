import numpy as np
import math
from  import dolaylıModel, dms_to_radian

# Sabit Noktalar
C1x, C1y = 21.94, 45.88
C2x, C2y = -13.11, -0.39

# Gözlemler
L1 = dms_to_radian(42.03069, 0, 0)
L2 = dms_to_radian(66.07014, 0, 0)
L3 = dms_to_radian(71.89783, 0, 0)
sig = dms_to_radian(0, 0, 2)

# Yaklaşık Koordinat
x0, y0 = 61.02, -26.27

def Tan(x1, y1, x2, y2):
    return math.atan2(y2 - y1, x2 - x1)

def Fx(x1, y1, x2, y2):
    dy = y2 - y1
    dx = x2 - x1
    return dy / (dx**2 + dy**2)

def Fy(x1, y1, x2, y2):
    dy = y2 - y1
    dx = x2 - x1
    return -dx / (dx**2 + dy**2)

# Türevler
A1x = Fx(x0, y0, C1x, C1y) - Fx(x0, y0, C2x, C2y)
A1y = Fy(x0, y0, C1x, C1y) - Fy(x0, y0, C2x, C2y)

A2x = Fx(C2x, C2y, C1x, C1y) - Fx(C2x, C2y, x0, y0)
A2y = Fy(C2x, C2y, C1x, C1y) - Fy(C2x, C2y, x0, y0)

A3x = Fx(C1x, C1y, x0, y0) - Fx(C1x, C1y, C2x, C2y)
A3y = Fy(C1x, C1y, x0, y0) - Fy(C1x, C1y, C2x, C2y)

A = np.array([
    [A1x, A1y],
    [A2x, A2y],
    [A3x, A3y]
])

W = np.array([
    [Tan(x0, y0, C1x, C1y) - Tan(x0, y0, C2x, C2y) - L1],
    [Tan(C2x, C2y, C1x, C1y) - Tan(C2x, C2y, x0, y0) - L2],
    [Tan(C1x, C1y, x0, y0) - Tan(C1x, C1y, C2x, C2y) - L3]
])

Cr = np.eye(3) * (sig ** 2)
yak = np.array([[x0], [y0]])
olc = np.array([[L1], [L2], [L3]])

# EKK çözümü
deltaCap, rCap, xCap, lCap, CxCap, CrCap, ClCap, sig2 = dolaylıModel(A, W, Cr, yak, olc, n=3, u=2)

print(f"deltaCap\n{deltaCap}")
print(f"rCap\n{rCap}")
print(f"lCap\n{lCap}")
print(f"CxCap\n{CxCap}")
print(f"CrCap\n{CrCap}")
print(f"ClCap\n{ClCap}")
print(f"sig2Cap\n{sig2}")
print(f"xCap\n{xCap}")
