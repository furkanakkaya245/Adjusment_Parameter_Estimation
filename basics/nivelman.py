# NİVELMAN
import numpy as np
from fonksiyon import EKK
# Sabit Noktalar
H1=340.59
H2=223.62
# Ölçümler
L1= -274.76
L2= 30.63
L3= -86.34
L4= 305.38
L5= 118.42
# Hata
sig=0.02

A=np.array([[-1,1],
            [-1,0],
            [-1,0],
            [0,-1],
            [0,-1]])
W=np.array([[-L1],
            [H1-L2],
            [H2-L3],
            [H1-L4],
            [H2-L5]])
Cr=np.eye(5)*(sig**2)
x0=np.array([[0],
             [0]])
l0=np.array([[L1],
             [L2],
             [L3],
             [L4],
             [L5]])
n=5
u=2
[xCap,CxCap,deltaCap,rCap,sig2,ClCap,CrCap,lCap]=EKK(A,W,Cr,x0,l0,n,u)
print(f"CxCap\n{CxCap}")
print(f"deltaCap\n{deltaCap}")
print(f"rCap\n{rCap}")
print(f"sig\n{sig}")
print(f"ClCap\n{ClCap}")
print(f"CrCap\n{CrCap}")
print(f"lCap\n{lCap}")
print(f"xCap\n{xCap}")



