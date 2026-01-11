import numpy as np
import  math 
import numpy.linalg
from numpy.linalg import inv
import genelFonk
from genelFonk import dolaylıModel, sartModel, dms_to_radian


# Soru1

# Tanımlamalar
x0 = np.array([[0], [10000]])
y0 = np.array([[0], [0]])
l0 = np.array([[8341.415], [9167.600], [dms_to_radian(60, 0, 0)]])
yakDeg = np.array([
    [l0[0][0] * math.cos(l0[2][0])],
    [l0[0][0] * math.sin(l0[2][0])]
])

d1 = math.hypot(yakDeg[0][0] - x0[0][0], yakDeg[1][0] - y0[0][0])
d2 = math.hypot(yakDeg[0][0] - x0[1][0], yakDeg[1][0] - y0[1][0])
# A matrisi (Jacobian benzeri)
dx = yakDeg[0][0] - x0[1][0]
dy = yakDeg[1][0] - y0[1][0]

A = np.array([
    [dx / d1, dy / d1],
    [dx / d2, dy / d2],
    [-dy / (d1**2), dx / (d1**2)]
])

# W matrisi (gözlem farkları)
W = np.array([
    [d1 - l0[0][0]],
    [d2 - l0[1][0]],
    [math.atan(dy / dx) - l0[2][0]]
])

# Gözlem kovaryans matrisi
var1 = (0.02)**2                 # mesafe hatası varyansı (m^2)
var2 = (dms_to_radian(0, 0, 1))**2  # açı hatası varyansı (rad^2)

Cr = np.diag([var1, var1, var2])
print(f"A matrisi\n {A}")
print()
print(f"W matrisi\n {W}")
print()
print(f"Cr matrisi\n{Cr}")
