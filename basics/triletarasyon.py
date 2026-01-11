import numpy as np
import math
from fonksiyon import EKK 
# Trileterasyon
# Sabit Noktalar
def mesafe(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    return math.hypot(dx,dy)
C1x= -58.47
C1y= -49.58
C2x= -87.92
C2y= -23.10
# Ölçüler
L1= 81.64
L2= 84.75
L3= 95.44
L4= 97.87
L5= 72.50
# Hata
sig=0.03
# Yaklaşık Değerler
P1x= 1.40
P1y= 10.34
P2x= -72.11
P2y= 47.49

dP1P2=mesafe(P1x, P1y, P2x, P2y)
dC1P1=mesafe(C1x, C1y, P1x, P1y)
dC2P1=mesafe(C2x, C2y, P1x, P1y)
dC1P2=mesafe(C1x, C1y, P2x, P2y)
dC2P2=mesafe(C2x, C2y, P2x, P2y)
# Türev
# L1
d1P1x=((P2x-P1x)*(-1))/(dP1P2)
d1P1y=((P2y-P1y)*(-1))/(dP1P2)
d1P2x=((P2x-P1x)*(1))/(dP1P2)
d1P2y=((P2y-P1y)*(1))/(dP1P2)
# L2
d2P1x=((P1x-C1x)*(1))/(dC1P1)
d2P1y=((P1y-C1y)*(1))/(dC1P1)
d2P2x=0
d2P2y=0
# L3
d3P1x=((P1x-C2x)*(1))/(dC2P1)
d3P1y=((P1y-C2y)*(1))/(dC2P1)
d3P2x=0
d3P2y=0
# L4
d4P1x=0
d4P1y=0
d4P2x=((P2x-C1x)*(1))/(dC1P2)
d4P2y=((P2y-C1y)*(1))/(dC1P2)
# L5
d5P1x=0
d5P1y=0
d5P2x=((P2x-C2x)*(1))/(dC2P2)
d5P2y=((P2y-C2y)*(1))/(dC2P2)


A=np.array([[d1P1x,d1P1y,d1P2x,d1P2y],
            [d2P1x,d2P1y,d2P2x,d2P2y],
            [d3P1x,d3P1y,d3P2x,d3P2y],
            [d4P1x,d4P1y,d4P2x,d4P2y],
            [d5P1x,d5P1y,d5P2x,d5P2y]])
W=np.array([[dP1P2-L1 ],
            [dC1P1-L2 ],
            [dC2P1-L3 ],
            [dC1P2-L4 ],
            [dC2P2-L5 ]])
Cr=np.eye(5)*(sig**2)
x0=np.array([[P1x],
             [P1y],
             [P2x],
             [P2y]])
l0=np.array([[L1],
             [L2],
             [L3],
             [L4],
             [L5]])
[xCap,CxCap,deltaCap,rCap,sig2,ClCap,CrCap,lCap]=EKK(A,W,Cr,x0,l0,n=5,u=4)
print(f"CxCap\n{CxCap}")
print(f"deltaCap\n{deltaCap}")
print(f"rCap\n{rCap}")
print(f"sig\n{sig2}")
print(f"ClCap\n{ClCap}")
print(f"CrCap\n{CrCap}")
print(f"lCap\n{lCap}")
print(f"xCap\n{xCap}")



