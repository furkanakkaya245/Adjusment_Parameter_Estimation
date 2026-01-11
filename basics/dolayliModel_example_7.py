import numpy as np
from genelFonk import dolaylıModel

# Tanımlar
# Verilen Noktalar
H1=394.06
H2=29.19
# Ölçümler
L1=175.63
L2=371.02
L3=6.16
L4=195.4
L5=-169.47
x0=np.array([[0],[0]])
l=np.array([[L1],[L2],[L3],[L4],[L5]])
n=5
u=2
# Modelin Kurulması
A=np.array([[-1,1],[-1,0],[-1,0],[0,-1],[0,-1]])
W=np.array([[-L1],[H1-L2],[H2-L3],[H1-L4],[H2-L5]])
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



