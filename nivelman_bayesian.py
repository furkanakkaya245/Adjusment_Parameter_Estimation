import numpy as np
from numpy.linalg import inv
from paramDic_2 import deltaCap_standart,deltaCap_Bayesian,xCap,Cr_,rCap_,CxCap_,C0

H1=360.33

L1=-240.04
L2=-326.69
L3=-37.43
L4=-86.65
L5=202.61
L6=289.27
sig=0.02

P0_1= 397.72
P0_2= 157.85
P0_3= 71.13
sig_param= 0.01

A=np.array([[-1,1,0],
            [-1,0,1],
            [-1,0,0],
            [0,-1,1],
            [0,-1,0],
            [0,0,-1]])
W=np.array([[-L1],
            [-L2],
            [H1-L3],
            [-L4],
            [H1-L5],
            [H1-L6]])
# A şıkkı:
Cr_A=Cr_(6,sig)
x0=np.array([[0],
             [0],
             [0]])
deltaCap_A=deltaCap_standart(A,Cr_A,W)
xCap_A=xCap(x0,deltaCap_A)
CxCap_A=CxCap_(A,Cr_A)
rCap_A=rCap_(A,deltaCap_A,W)
print("========================================")
print("=========== A Şıkkı Sonuçlar ===========")
print("========================================")
print(f"DeltaCap:\n{deltaCap_A}")
print(f"xCap:\n{xCap_A}")
print(f"CxCap:\n{CxCap_A}")
print(f"rCap:\n{rCap_A}")
print("========================================")

# B şıkkı:
Cr_B=Cr_(6,sig)
x0_bias=np.array([[P0_1],
             [P0_2],
             [P0_3]])
C0_b=C0(3,sig_param)
L0=np.array([[L1], [L2],[L3],[L4],[L5],[L6]])
W_bayes=A@x0_bias-L0+np.array([[0],[0],[H1],[0],[H1],[H1]])
deltaCap_b=deltaCap_Bayesian(A,Cr_B,W_bayes,C0_b)
xCap_b=xCap(x0_bias,deltaCap_b)
CxCap_b=CxCap_(A,Cr_B)
rCap_b=rCap_(A,deltaCap_b,W_bayes)
print("=========== B Şıkkı Sonuçlar ===========")
print("========================================")
print(f"DeltaCap:\n{deltaCap_b}")
print(f"xCap:\n{xCap_b}")
print(f"CxCap:\n{CxCap_b}")
print(f"rCap:\n{rCap_b}")
print("========================================")


