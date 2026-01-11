import math
import numpy as np
p1=0
p2=0
H1=340.59
H2=223.62

L1=-273.76
L2=30.63
L3=-86.34
L4=305.38
L5=118.42
L=np.array([[L1],[L2],[L3],[L4],[L5]])
A=np.array([[1,-1],[1,0],[1,0],[0,1],[0,1]])
transA=A.T
w=np.array([[0],[-H1],[-H2],[-H1],[-H2]])
Cr=np.array([[(0.02^2),0,0,0,0],[0,(0.02^2),0,0,0],[0,0,(0.02^2),0,0],[0,0,0,(0.02^2),0],
    [0,0,0,0,(0.02^2)]])
deltaKep=np.linalg.inv(transA@Cr@A)@transA@Cr@w
Ckep=np.linalg.inv(transA@Cr@A)
rkep=A@deltaKep+w
Lkep=L+rkep

