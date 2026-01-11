import numpy as np
from paramDic_2 import deltaCap_standart,xCap,Cr_,N_standart,C0,CxCap_,kosullu_deltaCap
from numpy.linalg import inv
H1= 240.96

L1= 88.92
L2= 18.93
L3= 40.11
L4= -69.98
L5= -48.81
L6= 21.17

sig=0.02

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
x0=np.array([[0],
             [0],
             [0]])
Cr=Cr_(6,sig)
deltaCap_Normal=deltaCap_standart(A,Cr,W)
xCap_Normal=xCap(x0,deltaCap_Normal)
CxCap_Normal=CxCap_(A,Cr)
print(f"deltacap_Normal:\n{deltaCap_Normal}\nxCap_normal:\n{xCap_Normal}\n\nCxCap_normal:\n{CxCap_Normal}")
########################################################
P1=200.0

Ac=np.array([[1,0,0]
            ])
Wc=np.array([[-200]])

deltaCap_kosul=kosullu_deltaCap(A,Ac,W,Wc,Cr,6,sig)
xCap_kosul=xCap(x0,deltaCap_kosul)
CxCap_kosul=CxCap_(A,Cr)
print(f"deltacap_kosul:\n{deltaCap_kosul}\nxCap_kosul:\n{xCap_kosul}\n\nCxCap_kosul:\n{CxCap_kosul}")


