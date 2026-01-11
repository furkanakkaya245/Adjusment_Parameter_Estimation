# Nirengi
import numpy as np
import math
from fonksiyon import EKK, dms_to_degree

def tan(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    return math.atan2(dx, dy)

def dTan(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    return 1/(1+((dx/dy)**2))
def Fx(x1,y1,x2,y2):
    return 1/(y2-y1)
def Fy(x1,y1,x2,y2):
    return -((x2-x1)/((y2-y1)**2))

# Sabitler
C1x=21.94
C1y=45.88
C2x=-13.11
C2y=-0.39
# Ölçüler
L1=dms_to_degree(42.03069)
L2=dms_to_degree(66.07014)
L3=dms_to_degree(71.89783)
# Hatalar
sig=dms_to_degree(0,0,2)
#Yaklaşık Değerler
Px=61.02
Py=-26.27

L1Px=((0.773165)*(0.01386)*(-1))-((0.108640)*(0.038639)*(-1))
L1Py=((0.773165)*(0.00750726)*(-1))-((0.108640)*(0.11067905)*(-1))

L2Px=-((0.773165)*(-0.01386)*(1))
L2Py=-((0.773165)*(-0.00750726)*(1))

L3Px=((0.108640)*(-0.038639)*(1))
L3Py=((0.108640)*(-0.11067905)*(1))

L1Px=dms_to_degree(L1Px)
L1Py=dms_to_degree(L1Py)

L2Px=dms_to_degree(L2Px)
L2Py=dms_to_degree(L2Py)

L3Px=dms_to_degree(L3Px)
L3Py=dms_to_degree(L3Py)


A=np.array([[L1Px,L1Py],
            [L2Px,L2Py],
            [L3Px,L3Py]])

W=np.array([[(dms_to_degree(42.312920))-L1],
            [(dms_to_degree(65.586438))-L2 ],
            [(dms_to_degree(107.899359))-L3 ]])
Cr=np.eye(3)*(sig**2)
x0=np.array([[Px],
             [Py]])
l0=np.array([[L1],
             [L2],
             [L3]])
[xCap,CxCap,deltaCap,rCap,sig2,ClCap,CrCap,lCap]=EKK(A,W,Cr,x0,l0,n=3,u=2)
print(f"CxCap\n{CxCap}")
print(f"deltaCap\n{deltaCap}")
print(f"rCap\n{rCap}")
print(f"sig\n{sig2}")
print(f"ClCap\n{ClCap}")
print(f"CrCap\n{CrCap}")
print(f"lCap\n{lCap}")
print(f"xCap\n{xCap}")




