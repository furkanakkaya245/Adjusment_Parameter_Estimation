import numpy as np
from paramDic_2 import deltaCap_Bayesian,xCap,Cr_,N_standart,C0,CxCap_,kosullu_deltaCap
from numpy.linalg import inv
H1= 178.06
H2= 117.84
H3= 204.81

L1= 114.51
L2= 5.62
L3= -54.59
L4= 32.38
L5= -108.89
L6= -169.10
L7= -82.13
sig=0.02

P1_0=171.91
P2_0=287.32
sig_param=1.00

A=np.array([[-1,1],
            [-1,0],
            [-1,0],
            [-1,0],
            [0,-1],
            [0,-1],
            [0,-1]])
W=np.array([[-L1],
            [H1-L2],
            [H2-L3],
            [H3-L4],
            [H1-L5],
            [H2-L6],
            [H3-L7]])
x0=np.array([[P1_0],
             [P2_0]])
Cr=Cr_(7,sig)
C0_=C0(2,sig_param)
deltaCap_Normal=deltaCap_Bayesian(A,Cr,W,C0_)
xCap_Normal=xCap(x0,deltaCap_Normal)
CxCap_Normal=CxCap_(A,Cr)
print("========================================")
print("=========== A Şıkkı Sonuçlar ===========")
print("========================================")
print(f"deltacap_Normal:\n{deltaCap_Normal}\nxCap_normal:\n{xCap_Normal}\n\nCxCap_normal:\n{CxCap_Normal}")
########################################################
P1=172.33

Ac=np.array([[-1,0]])
Wc=np.array([[H1-L2]])
print("========================================")
print("=========== B Şıkkı Sonuçlar ===========")
print("========================================")
deltaCap_kosul=kosullu_deltaCap(A,Ac,W,Wc,Cr,7,sig)
xCap_kosul=xCap(x0,deltaCap_kosul)
CxCap_kosul=CxCap_(A,Cr)
print(f"deltacap_kosul:\n{deltaCap_kosul}\nxCap_kosul:\n{xCap_kosul}\nCxCap_kosul:\n{CxCap_kosul}")


