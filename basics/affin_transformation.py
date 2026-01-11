# Affin Dönüşümü
import numpy as np
import math
from fonksiyon import EKK, dms_to_degree

# Sabitler
P1x= 5.99
P1y=-21.10
P2x=-52.34
P2y=-33.06
P3x= 29.39
P3y= 22.82
P4x=-61.05
P4y= 48.22
P5x= 82.24
P5y=-41.69
P6x= 97.99
P6y= 32.66
# ölçüler
L1x= 11.73
L1y=-29.51
L2x=-31.64
L2y=-48.48
L3x= 22.10
L3y= 24.51
L4x=-54.63
L4y= 47.05
L5x= 76.26
L5y=-47.53
L6x= 74.83
L6y= 41.90
# Yaklaşık Değerler
x0=0
y0=0
k=0
phi=0
A=np.array([[1 ,0 ,(P1x*math.cos(phi)+P1y*math.sin(phi)) , (-P1x*(1+k)*math.sin(phi)+P1y*(1+k)*math.cos(phi)) ],
            [0 ,1 ,(-P1x*math.sin(phi)+P1y*math.cos(phi)) , (-P1x*(1+k)*math.cos(phi)-P1y*(1+k)*math.sin(phi)) ],
            [1 ,0 ,(P2x*math.cos(phi)+P2y*math.sin(phi)) , (-P2x*(1+k)*math.sin(phi)+P2y*(1+k)*math.cos(phi)) ],
            [0 ,1 ,(-P2x*math.sin(phi)+P2y*math.cos(phi)) , (-P2x*(1+k)*math.cos(phi)-P2y*(1+k)*math.sin(phi)) ],
            [1 ,0 ,(P3x*math.cos(phi)+P3y*math.sin(phi)) , (-P3x*(1+k)*math.sin(phi)+P3y*(1+k)*math.cos(phi)) ],
            [0 ,1 ,(-P3x*math.sin(phi)+P3y*math.cos(phi)) , (-P3x*(1+k)*math.cos(phi)-P3y*(1+k)*math.sin(phi)) ],
            [1 ,0 ,(P4x*math.cos(phi)+P4y*math.sin(phi)) , (-P4x*(1+k)*math.sin(phi)+P4y*(1+k)*math.cos(phi)) ],
            [0 ,1 ,(-P4x*math.sin(phi)+P4y*math.cos(phi)) , (-P4x*(1+k)*math.cos(phi)-P4y*(1+k)*math.sin(phi)) ],
            [1 ,0 ,(P5x*math.cos(phi)+P5y*math.sin(phi)) , (-P5x*(1+k)*math.sin(phi)+P5y*(1+k)*math.cos(phi)) ],
            [0 ,1 ,(-P5x*math.sin(phi)+P5y*math.cos(phi)) , (-P5x*(1+k)*math.cos(phi)-P5y*(1+k)*math.sin(phi)) ],
            [1 ,0 ,(P6x*math.cos(phi)+P6y*math.sin(phi)) , (-P6x*(1+k)*math.sin(phi)+P6y*(1+k)*math.cos(phi)) ],
            [0 ,1 ,(-P6x*math.sin(phi)+P6y*math.cos(phi)) , (-P6x*(1+k)*math.cos(phi)-P6y*(1+k)*math.sin(phi)) ]])
W = np.array([
    [x0 + (P1x*(1+k)*math.cos(phi)) + (P1y*(1+k)*math.sin(phi))],
    [y0 + (-P1x*(1+k)*math.sin(phi)) + (P1y*(1+k)*math.cos(phi))],
    [x0 + (P2x*(1+k)*math.cos(phi)) + (P2y*(1+k)*math.sin(phi))],
    [y0 + (-P2x*(1+k)*math.sin(phi)) + (P2y*(1+k)*math.cos(phi))],
    [x0 + (P3x*(1+k)*math.cos(phi)) + (P3y*(1+k)*math.sin(phi))],
    [y0 + (-P3x*(1+k)*math.sin(phi)) + (P3y*(1+k)*math.cos(phi))],
    [x0 + (P4x*(1+k)*math.cos(phi)) + (P4y*(1+k)*math.sin(phi))],
    [y0 + (-P4x*(1+k)*math.sin(phi)) + (P4y*(1+k)*math.cos(phi))],
    [x0 + (P5x*(1+k)*math.cos(phi)) + (P5y*(1+k)*math.sin(phi))],
    [y0 + (-P5x*(1+k)*math.sin(phi)) + (P5y*(1+k)*math.cos(phi))],
    [x0 + (P6x*(1+k)*math.cos(phi)) + (P6y*(1+k)*math.sin(phi))],
    [y0 + (-P6x*(1+k)*math.sin(phi)) + (P6y*(1+k)*math.cos(phi))]])
Cr=np.eye(12)
x0=np.array([[0],
             [0],
             [0],
             [0]])
l0=np.array([[L1x],
             [L1y],
             [L2x],
             [L2y],
             [L3x],
             [L3y],
             [L4x],
             [L4y],
             [L5x],
             [L5y],
             [L6x],
             [L6y]])
[xCap,CxCap,deltaCap,rCap,sig2,ClCap,CrCap,lCap]=EKK(A,W,Cr,x0,l0,n=12,u=4)
print(f"CxCap\n{CxCap}")
print(f"deltaCap\n{deltaCap}")
print(f"rCap\n{rCap}")
print(f"sig\n{sig2}")
print(f"ClCap\n{ClCap}")
print(f"CrCap\n{CrCap}")
print(f"lCap\n{lCap}")
print(f"xCap\n{xCap}")









