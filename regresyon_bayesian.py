import numpy as np
from paramDic_2 import deltaCap_standart,deltaCap_Bayesian,xCap,Cr_,rCap_,CxCap_,C0

x01= -98.39
y01= -90.46
x02= -38.05
y02= -9.82
x03= 2.79
y03= 92.34
x04= 54.63
y04= 153.07
x05= 74.09
y05= 174.45
sig=50

a0_0= 65.00
a1_0= 1.50
sig_a0= 5.0
sig_a1= 0.3

A = np.array([[1, x01], 
              [1, x02], 
              [1, x03], 
              [1, x04], 
              [1, x05]])
W = np.array([[-y01], 
              [-y02], 
              [-y03], 
              [-y04], 
              [-y05]])

# A şıkkı:
Cr_A=Cr_(5,sig)
x0=np.array([[0],
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
Cr_B=Cr_(5,sig)
x0_bias=np.array([[a0_0],
             [a1_0]])
C0_b=C0(2,sig_a0)
C0_b[1][1]=sig_a1**2
L0=np.array([[y01], [y02],[y03],[y04],[y05]])
W_bayes=A@x0_bias-L0+np.array([[0],[0],[0],[0],[0]])
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




