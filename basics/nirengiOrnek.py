import numpy as np
import math
from genelFonk import dolaylıModel, dms_to_radian, degree_to_dms
# Nirengi Ağı
# Tanımlamalar
C1x= 21.94
C1y= 45.88
C2x= -13.11
C2y= -0.39
# Ölçüler

L1=dms_to_radian(42.03069, 0, 0)
L2=dms_to_radian(66.07014, 0, 0)
L3=dms_to_radian(71.89783, 0, 0)

sig= dms_to_radian(0, 0, 2)
# Yaklaşık Noktalar
x0= 61.02
y0= -26.27
def Tan(x1,y1,x2,y2):
    return math.atan2(y2 - y1, x2 - x1)

def tanEleman(x1,y1,x2,y2):
    m=1+(((x1-x2)/(y1-y2))**2)
    return 1/m
def Fx(x1,y1,x2,y2):
    return 1/(y1-y2)
def Fy(x1,y1,x2,y2):
    return (x1-x2)/((y1-y2)**2)

A1x=tanEleman(C1x, C1y, x0, y0)*Fx(C1x, C1y, x0, y0)-tanEleman(C2x, C2y, x0, y0)*Fx(C2x, C2y, x0, y0)
A1y=tanEleman(C1x, C1y, x0, y0)*Fy(C1x, C1y, x0, y0)-tanEleman(C2x, C2y, x0, y0)*Fy(C2x, C2y, x0, y0)

A2x=tanEleman(x0, y0, C1x, C1y)*Fx(x0, y0, C1x, C1y)
A2y=tanEleman(x0, y0, C1x, C1y)*Fy(x0, y0, C1x, C1y)

A3x=tanEleman(x0, y0, C2x, C2y)*Fx(x0, y0, C2x, C2y)
A3y=tanEleman(x0, y0, C2x, C2y)*Fy(x0, y0, C2x, C2y)

# Modelin Kurulması
A=np.array([[A1x,A1y],
            [A2x,A2y],
            [A3x,A3y]]) 
W=np.array([[Tan(C1x, C1y, x0, y0)-Tan(C2x, C2y, x0, y0)-L1],
            [Tan(C2x, C2y, C1x, C1y)-Tan(x0, y0, C1x, C1y)-L2],
            [Tan(x0, y0, C2x, C2y)-Tan(C1x, C1y, C2x, C2y)-L3]])
Cr=np.eye(3)*(sig**2)
n=3
u=2
yak=np.array([[x0],
              [y0]])
olc=np.array([[L1],
              [L2],
              [L3]])
[deltaCap,rCap,xCap,lCap,CxCap,CrCap,ClCap,sig2]=dolaylıModel(A, W, Cr, yak, olc, n, u)
print(f"deltaCap\n{deltaCap}")
print(f"rCap\n{rCap}")
print(f"lCap\n{lCap}")
print(f"CxCap\n{CxCap}")
print(f"CrCap\n{CrCap}")
print(f"ClCap\n{ClCap}")
print(f"sig2Cap\n{sig2}")
print(f"xCap\n{xCap}")







