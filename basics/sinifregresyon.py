# Regresyon 
import numpy as np
import math
from fonksiyon import EKK
# Sabitler
x1=-78.26
x2=-72.10
x3=-57.84
x4=-49.11
x5=-0.66
x6=2.61
x7=15.38
x8=52.78
x9=63.88
x10=80.98
# Ölçüler
L1= -22.03
L2=8.00
L3=-4.90
L4=14.20
L5=42.03
L6=31.63
L7=67.97
L8=91.65
L9=80.14
L10=102.40
# hata
sig=0.5

A=np.array([[1, x1],
            [1, x2],
            [1, x3],
            [1, x4],
            [1, x5],
            [1, x6],
            [1, x7],
            [1, x8],
            [1, x9],
            [1, x10]])
W=np.array([[-L1],
            [-L2],
            [-L3],
            [-L4],
            [-L5],
            [-L6],
            [-L7],
            [-L8],
            [-L9],
            [-L10]])
Cr=np.eye(10)*(sig**2)
x0=np.array([[0],
             [0]])
l0=np.array([[L1],
            [L2],
            [L3],
            [L4],
            [L5],
            [L6],
            [L7],
            [L8],
            [L9],
            [L10]])
[xCap,CxCap,deltaCap,rCap,sig2,ClCap,CrCap,lCap]=EKK(A,W,Cr,x0,l0,n=10,u=2)
print(f"CxCap\n{CxCap}")
print(f"deltaCap\n{deltaCap}")
print(f"rCap\n{rCap}")
print(f"sig\n{sig2}")
print(f"ClCap\n{ClCap}")
print(f"CrCap\n{CrCap}")
print(f"lCap\n{lCap}")
print(f"xCap\n{xCap}")



