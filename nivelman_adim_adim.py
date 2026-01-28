import numpy as np
from numpy.linalg import inv
from paramDic_2 import Direkt_AdimAdim_Cozum

H1=321.60

L1=247.86
L2=33.90
L3=215.08
L4=-213.97
L5=-32.78
L6=181.19
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
cozum=Direkt_AdimAdim_Cozum(4,6,A,W,sig)
print(f"deltaCap_normal:\n{cozum.deltaCap()}")
print(f"deltaCap_direkt:\n{cozum.direktDeltaCapSon()}")
print(f"deltaCap_birlikte:\n{cozum.birliteDeltaCapSon()}")


