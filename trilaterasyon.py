import numpy as np
import math
from numpy.linalg import inv
from paramDic_2 import Cr_,deltaCap_standart,xCap,dms_to_radian,N_standart
def mesafe(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    return math.hypot(dx,dy)

C1x=8.74
C1y=-22.18
C2x= -99.01
C2y= -37.82
L1= 92.48
L2= 86.67
L3= 52.45
L4= 34.41
L5= 128.17
sig_olcu= 0.03
P1x=-72.73
P1y=7.75
P2x=18.92
P2y=9.58
sig_param=0.5

dP2P1=mesafe(P2x, P2y, P1x, P1y)
dC1P1=mesafe(C1x, C1y, P1x, P1y)
dC2P1=mesafe(C2x, C2y, P1x, P1y)
dC1P2=mesafe(C1x, C1y, P2x, P2y)
dC2P2=mesafe(C2x, C2y, P2x, P2y)
# Türev
# L1
d1P1x=((P2x-P1x)*(-1))/(dP2P1)
d1P1y=((P2y-P1y)*(-1))/(dP2P1)
d1P2x=((P2x-P1x)*(1))/(dP2P1)
d1P2y=((P2y-P1y)*(1))/(dP2P1)
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
W=np.array([[dP2P1-L1 ],
            [dC1P1-L2 ],
            [dC2P1-L3 ],
            [dC1P2-L4 ],
            [dC2P2-L5 ]])
Cr=Cr_(5,sig_olcu)
x0_normal=np.array([[P1x],
             [P1y],
             [P2x],
             [P2y]])
l0=np.array([[L1],
             [L2],
             [L3],
             [L4],
             [L5]])
deltaCap_Normal=deltaCap_standart(A,Cr,W)
xCap_Normal=xCap(x0_normal,deltaCap_Normal)
print(f"deltaCap_Normal:\n{deltaCap_Normal}\nxCap:\n{xCap_Normal}\n")
#######################################################################
# 1. Koşul P1-P2=85 azimut farkına göre
d0=mesafe(P1x,P1y,P2x,P2y)
aci=dms_to_radian(85,0,0)

dP1x= -(P2x-P1x)/(d0**2)
dP1y= -(P2y-P1y)/(d0**2)
dP2x= (P2x-P1x)/(d0**2)
dP2y= (P2y-P1y)/(d0**2)

Ac=np.array([[dP1x,
             dP1y,
             dP2x,
             dP2y]])
FarkX=P2x-P1x
FarkY=P2y-P1y
oranFark=FarkX/FarkY
Wc=np.array([[np.atan2(FarkX,FarkY)-aci]])
#Wc=np.array([[np.atan(oranFark)-aci]])
deltaCap_kosul = deltaCap_Normal - inv(N_standart(A,Cr)) @ Ac.T @ np.linalg.inv(Ac @ inv(N_standart(A,Cr)) @ Ac.T) @ (Wc + Ac @ deltaCap_Normal)
xCap_kosul = x0_normal + deltaCap_kosul
print(f"deltacap_kosul:\n{deltaCap_kosul}\nxCap_kosul:\n{xCap_kosul}\n")

