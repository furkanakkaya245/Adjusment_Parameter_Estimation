import numpy as np
import math
from genelFonk import dolaylıModel, dms_to_radian

def Tan(x1,y1,x2,y2):
    return math.atan2(y2 - y1, x2 - x1)

def Fx(x1, y1, x2, y2):
    return (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)

def Fy(x1, y1, x2, y2):
    return -(x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)


C1=np.array([[0],[0]])
C2=np.array([[10000],[0]])

L1=8341.415
L2=9167.600
L3=dms_to_radian(59, 9, 20)

x0=L1*math.cos(L3)
y0=L1*math.sin(L3)

d1x=x0-C1[0][0]
d1y=y0-C1[1][0]
d2x=x0-C2[0][0]
d2y=y0-C2[1][0]
d1p=math.hypot(d1x,d1y)
d2p=math.hypot(d2x,d2y)
d3_0=Tan(C2[0][0], C2[1][0], C1[0][0], C1[1][0])-Tan(x0, y0, C1[0][0], C1[1][0])
d3x= -Fx(x0, y0, C1[0][0], C1[1][0])
d3y= -Fy(x0, y0, C1[0][0], C1[1][0])

A=np.array([[d1x/d1p,d1y/d1p],
            [d2x/d2p,d2y/d2p],
            [d3x,d3y]])
W=np.array([[d1p-L1],
            [d2p-L2],
            [d3_0-L3]])

Cr=np.eye(3)
Cr[0][0]=0.02**2
Cr[1][1]=0.02**2
Cr[2][2]=dms_to_radian(0, 0, 1)**2
x0=np.array([[x0],[y0]])
l=np.array([[L1],[L2],[L3]])
n=3
u=2
[deltaCap,rCap,xCap,lCap,CxCap,CrCap,ClCap,sig2]=dolaylıModel(A, W, Cr, x0, l, n, u)
print(f"deltaCap\n{deltaCap}")
print(f"rCap\n{rCap}")
print(f"lCap\n{lCap}")
print(f"CxCap\n{CxCap}")
print(f"CrCap\n{CrCap}")
print(f"ClCap\n{ClCap}")
print(f"sig2Cap\n{sig2}")
print(f"xCap\n{xCap}")



