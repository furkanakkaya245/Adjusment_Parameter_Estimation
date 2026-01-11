import numpy as np
from genelFonk import dolaylıModel
# Nivelman Ağı
# Tanımlar
# Verilen Noktalar
H1=394.06
H1=340.59
H2=223.62
# Ölçümler
L1=-274.76
L2=30.63
L3=-86.34
L4=305.38
L5=188.42

x0=np.array([[0],[0]])
l=np.array([[L1],[L2],[L3],[L4],[L5]])
n=5
u=2
# Modelin Kurulması
A=np.array([[-1,1],
            [-1,0],
            [-1,0],
            [0,-1],
            [0,-1],
            ])
W=np.array([[-L1],
            [H1-L2],
            [H2-L3],
            [H1-L4],
            [H2-L5],
            ])
Cr=np.eye(5)*(0.02**2)

[deltaCap,rCap,xCap,lCap,CxCap,CrCap,ClCap,sig2]=dolaylıModel(A, W, Cr, x0, l, n, u)
print(f"deltaCap\n{deltaCap}")
print(f"rCap\n{rCap}")
print(f"lCap\n{lCap}")
print(f"CxCap\n{CxCap}")
print(f"CrCap\n{CrCap}")
print(f"ClCap\n{ClCap}")
print(f"sig2Cap\n{sig2}")
print(f"xCap\n{xCap}")


