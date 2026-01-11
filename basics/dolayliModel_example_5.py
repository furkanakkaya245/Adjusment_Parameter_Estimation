import numpy as np
import math
from genelFonk import dolaylıModel
#affin

# Affin fonksiyonlar
def Kx(PiX,PiY,phi):
    return PiX*math.cos(phi)-PiY*math.sin(phi)
def Ky(PiX,PiY,phi):
    return PiX*math.sin(phi)+PiY*math.cos(phi)
def phiX(PiX,PiY,phi,k):
    return (1+k)*(PiX*math.sin(phi)+PiY*math.cos(phi))
def phiY(PiX,PiY,phi,k):
    return -(1+k)*(PiX*math.cos(phi)-PiY*math.sin(phi))
def f0x(x0,Pix,Piy,phi,k,Lix):
    return (x0+(1+k)*(Pix*math.cos(phi)+Piy*math.sin(phi)))-Lix
def f0y(y0,Pix,Piy,phi,k,Liy):
    return (y0+(1+k)*(-Pix*math.sin(phi)+Piy*math.cos(phi)))-Liy

# Noktalar
P = np.array([[5.99, -21.10],
              [-51.34, -33.06],
              [29.39, 22.82],
              [-61.05, 48.22],
              [82.24, -41.69],
              [97.99, 32.66]])

L = np.array([[11.73, -29.51],
              [-31.64, -48.48],
              [22.10, 24.51],
              [-54.63, 47.05],
              [76.26, -47.53],
              [74.83, 41.90]])

olc = L.reshape(-1, 1)
n = 12
u = 4


phi0 = 0
k0 = 0
x0 = L[4,0] - ((1 + k0) * (P[4,0]*math.cos(phi0) - P[4,1]*math.sin(phi0)))
y0 = L[4,1] - ((1 + k0) * (P[4,0]*math.sin(phi0) + P[4,1]*math.cos(phi0)))
yak = np.array([[x0],[y0],[k0],[phi0]])

A = []
W = []

for i in range(6):
    PiX, PiY = P[i]
    Lix, Liy = L[i]

    A.append([1, 0, Kx(PiX, PiY, phi0), phiX(PiX, PiY, phi0, k0)])
    A.append([0, 1, Ky(PiX, PiY, phi0), phiY(PiX, PiY, phi0, k0)])

    W.append([f0x(x0, PiX, PiY, phi0, k0, Lix)])
    W.append([f0y(y0, PiX, PiY, phi0, k0, Liy)])

A = np.array(A)
W = np.array(W)
Cr = np.eye(12)

[deltaCap,rCap,xCap,lCap,CxCap,CrCap,ClCap,sig2]=dolaylıModel(A, W, Cr, yak, olc, n, u)
print(f"deltaCap\n{deltaCap}")
print(f"rCap\n{rCap}")
print(f"lCap\n{lCap}")
print(f"CxCap\n{CxCap}")
print(f"CrCap\n{CrCap}")
print(f"ClCap\n{ClCap}")
print(f"sig2Cap\n{sig2}")
print(f"xCap\n{xCap}")


