import numpy as np
from genelFonk import dolaylıModel
# Nivelman Ağı
# Tanımlar
# Verilen Noktalar
H1=154.42
H2=340.66
# Ölçümler
L1= -103.35
L2= -99.24
L3= -222.46
L4= -36.22
L5= 4.11
L6= -119.11
L7= 67.12
L8= -123.22
L9= 63.01
x0=np.array([[0],[0],[0]])
l=np.array([[L1],[L2],[L3],[L4],[L5],[L6],[L7],[L8],[L9]])
n=9
u=3
# Modelin Kurulması
A=np.array([[-1,1,0],
            [-1,0,1],
            [-1,0,0],
            [-1,0,0],
            [0,-1,1],
            [0,-1,0],
            [0,-1,0],
            [0,0,-1],
            [0,0,-1]])
W=np.array([[-L1],
            [-L2],
            [H1-L3],
            [H2-L4],
            [-L5],
            [H1-L6],
            [H2-L7],
            [H1-L8],
            [H2-L9]])
Cr=np.eye(9)*(0.02**2)
[deltaCap,rCap,xCap,lCap,CxCap,CrCap,ClCap,sig2]=dolaylıModel(A, W, Cr, x0, l, n, u)
print(f"deltaCap\n{deltaCap}")
print(f"rCap\n{rCap}")
print(f"lCap\n{lCap}")
print(f"CxCap\n{CxCap}")
print(f"CrCap\n{CrCap}")
print(f"ClCap\n{ClCap}")
print(f"sig2Cap\n{sig2}")
print(f"xCap\n{xCap}")


