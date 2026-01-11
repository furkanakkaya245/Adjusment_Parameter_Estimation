import numpy as np
from paramDic_2 import trilaterasyon_cozum as tc
from paramDic_2 import Cr_,deltaCap_standart,xCap,deltaCap_Bayesian,C0
from paramDic_2 import Direkt_AdimAdim_Cozum_Trilaterasyon as adimadim
from paramDic_2 import deltaCap_standart,CxCap_


C1x=-90.2
C1y=-21.15
C2x=-38.39
C2y=8.35
C3x=51.94
C3y=-11.61
C4x=82.57
C4y=26.08
C5x=84.59
C5y=-42.98

L1=45.65
L2=48.33
L3=103.68
L4=145.99
L5=132.75
sig_olcum=0.03

P1x=-48.41
P1y=-39.46


dL1=tc(P1x,P1y,C1x,C1y).turev()
dL2=tc(P1x,P1y,C2x,C2y).turev()
dL3=tc(P1x,P1y,C3x,C3y).turev()
dL4=tc(P1x,P1y,C4x,C4y).turev()
dL5=tc(P1x,P1y,C5x,C5y).turev()

d0_1=tc(P1x,P1y,C1x,C1y).d0()
d0_2=tc(P1x,P1y,C2x,C2y).d0()
d0_3=tc(P1x,P1y,C3x,C3y).d0()
d0_4=tc(P1x,P1y,C4x,C4y).d0()
d0_5=tc(P1x,P1y,C5x,C5y).d0()

A=np.array([[dL1[0],dL1[1]],
            [dL2[0],dL2[1]],
            [dL3[0],dL3[1]],
            [dL4[0],dL4[1]],
            [dL5[0],dL5[1]]])
W=np.array([[d0_1-L1],
            [d0_2-L2],
            [d0_3-L3],
            [d0_4-L4],
            [d0_5-L5]])

x0=np.array([[P1x],
             [P1y]])
W1=W[:3:]
W2=W[3:5:]
A1=A[:3:]
A2=A[3:5:]

# A
Cr_a=Cr_(3,sig_olcum)
deltaCap_a=deltaCap_standart(A1,Cr_a,W1)
xCap_a=xCap(x0,deltaCap_a)
CxCap_a=CxCap_(A1,Cr_a)
print(f"deltaCap_a:\n{deltaCap_a}\nxCap_a:\n{xCap_a}\nCxCap_a:\n{CxCap_a}")

# B
Cr_b=Cr_(2,sig_olcum)
deltaCap_b=adimadim(3,2,A,W,sig_olcum).birliteDeltaCapSon()
xCap_b=xCap(x0,deltaCap_b)
CxCap_b=CxCap_(A2,Cr_b)
print(f"deltaCap_b:\n{deltaCap_b}\nxCap_b:\n{xCap_b}\nCxCap_b:\n{CxCap_b}")

# C
Cr_c=Cr_(5,sig_olcum)
deltaCap_c=adimadim(3,2,A,W,sig_olcum).direktDeltaCapSon()
xCap_c=xCap(x0,deltaCap_c)
CxCap_c=CxCap_(A,Cr_c)

print(f"deltaCap_c:\n{deltaCap_c}\nxCap_c:\n{xCap_c}\nCxCap_c:\n{CxCap_c}")




