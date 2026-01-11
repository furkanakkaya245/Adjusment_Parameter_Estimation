import numpy as np
import math
from genelFonk import dolaylıModel
# Trilaterasyon Ağı
# Tanımlamalar
# Sabit Noktalar
C1x= -50.77
C1y= -41.65
C2x= -10.20
C2y= -33.74
# Ölçüler
L1= 109.32
L2= 82.63
L3= 106.92
L4= 96.87
L5= 70.72
# Hata
sig=0.03
# Yaklaşık Değerler
P1x= -100.20
P1y= 25.86
P2x= 10.02
P2y= 33.76
# Modelin Kurulması
d1x=P2x-P1x
d2x=C1x-P1x
d3x=C2x-P1x
d4x=C1x-P2x
d5x=P2x-C2x
d1y=P2y-P1y
d2y=C1y-P1y
d3y=C2y-P1y
d4y=C1y-P2y
d5y=P2y-C2y
# Uzaklık Tanımlama
d1=math.hypot(d1x,d1y)
d2=math.hypot(d2x,d2y)
d3=math.hypot(d3x,d3y)
d4=math.hypot(d4x,d4y)
d5=math.hypot(d5x,d5y)

A=np.array([[-(P2x-P1x),-(P2y-P1y),(P2x-P1x),(P2y-P1y)],
            [(P1x-C1x),(P1y-C1y),(0),(0)],
            [(P1x-C2x),(P1y-C2y),(0),(0)],
            [(0),(0),(P2x-C1x),(P2y-C1y)],
            [(0),(0),(P2x-C2x),(P2y-C2y)]])
W=np.array([[d1-L1],
            [d2-L2],
            [d3-L3],
            [d4-L4],
            [d5-L5]])
Cr=np.eye(5)*(sig**2)
n=5
u=4
x0=np.array([[P1x],
             [P1y],
             [P2x],
             [P2y]])
l=np.array([[L1],
            [L2],
            [L3],
            [L4],
            [L5]])
[deltaCap,rCap,xCap,lCap,CxCap,CrCap,ClCap,sig2]=dolaylıModel(A, W, Cr, x0, l, n, u)
print(f"deltaCap\n{deltaCap}")
print(f"rCap\n{rCap}")
print(f"lCap\n{lCap}")
print(f"CxCap\n{CxCap}")
print(f"CrCap\n{CrCap}")
print(f"ClCap\n{ClCap}")
print(f"sig2Cap\n{sig2}")
print(f"xCap\n{xCap}")

























