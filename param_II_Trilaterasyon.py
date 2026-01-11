import numpy as np
import math
from paramDic_2 import deltaCap_standart,xCap,Cr_
def fark(x1,y1,x0,y0):
    Dx=x0-x1
    Dy=y0-y1
    return Dx,Dy
def turev(Dx,Dy,mesafe):
    Dxx=Dx/mesafe
    Dyy=Dy/mesafe
    return Dxx, Dyy
def mesafe(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    return math.hypot(dx,dy)
C1x= -90.20
C1y= -21.15
C2x= -38.39
C2y= 8.35
C3x= 51.94
C3y= -11.61
C4x= 82.57
C4y= 26.08

L1=176.32
L2=133.42
L3=45.44
L4=69.14
sig=0.03

P1_0x=83.30
P1_0y=-42.79

C1_P1=mesafe(C1x,C1y,P1_0x,P1_0y)
C2_P1=mesafe(C2x,C2y,P1_0x,P1_0y)
C3_P1=mesafe(C3x,C3y,P1_0x,P1_0y)
C4_P1=mesafe(C4x,C4y,P1_0x,P1_0y)

D_C1_P1_x=fark(C1x,C1y,P1_0x,P1_0y)[0]
D_C1_P1_y=fark(C1x,C1y,P1_0x,P1_0y)[1]
D_C2_P1_x=fark(C2x,C2y,P1_0x,P1_0y)[0]
D_C2_P1_y=fark(C2x,C2y,P1_0x,P1_0y)[1]
D_C3_P1_x=fark(C3x,C3y,P1_0x,P1_0y)[0]
D_C3_P1_y=fark(C3x,C3y,P1_0x,P1_0y)[1]
D_C4_P1_x=fark(C4x,C4y,P1_0x,P1_0y)[0]
D_C4_P1_y=fark(C4x,C4y,P1_0x,P1_0y)[1]

dL1_x=turev(D_C1_P1_x,D_C1_P1_y,C1_P1)[0]
dL1_y=turev(D_C1_P1_x,D_C1_P1_y,C1_P1)[1]
dL2_x=turev(D_C2_P1_x,D_C2_P1_y,C2_P1)[0]
dL2_y=turev(D_C2_P1_x,D_C2_P1_y,C2_P1)[1]
dL3_x=turev(D_C3_P1_x,D_C3_P1_y,C3_P1)[0]
dL3_y=turev(D_C3_P1_x,D_C3_P1_y,C3_P1)[1]
dL4_x=turev(D_C4_P1_x,D_C4_P1_y,C4_P1)[0]
dL4_y=turev(D_C4_P1_x,D_C4_P1_y,C4_P1)[1]

# A
A=np.array([[dL1_x,dL1_y],
            [dL2_x,dL2_y],
            [dL3_x,dL3_y]])
W=np.array([[C1_P1-L1],
            [C2_P1-L2],
            [C3_P1-L3]])
x0=np.array([[P1_0x],
             [P1_0y]])
Cr=Cr_(3,sig)
deltaCap=deltaCap_standart(A,Cr,W)
xCap_=xCap(x0,deltaCap)
print(f"deltaCap_A:\n{deltaCap}")
print(f"xCap_A:\n{xCap_}")
# B
A=np.array([[dL1_x,dL1_y],
            [dL2_x,dL2_y],
            [dL3_x,dL3_y],
            [dL4_x,dL4_y]])
W=np.array([[C1_P1-L1],
            [C2_P1-L2],
            [C3_P1-L3],
            [C4_P1-L4]])
x0=np.array([[P1_0x],
             [P1_0y]])
Cr=Cr_(4,sig)
deltaCap=deltaCap_standart(A,Cr,W)
xCap_=xCap(x0,deltaCap)
print(f"deltaCap_B:\n{deltaCap}")
print(f"xCap_B:\n{xCap_}")















