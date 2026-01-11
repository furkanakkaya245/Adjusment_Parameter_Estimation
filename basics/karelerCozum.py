import numpy as np
from numpy.linalg import inv
H1=394.06
H2=29.19
L1=175.63
L2=371.02
L3=6.16
L4=195.4
L5=-169.47
def EKK(A,W,Cr,x0):
    CrInv=inv(Cr)
    CxCap=inv(A.T@CrInv@A)
    deltaCap=-1*(inv(A.T@CrInv@A)@A.T@CrInv@W)
    rCap=A@deltaCap+W
    xCap=x0+deltaCap
    Ninv=inv(A.T@CrInv@A)
    CrCap=Cr-(A@Ninv@A.T)
    ClCap=A@Ninv@A.T
    sig02=(rCap.T@CrInv@rCap)/(5-2)
    return xCap,CxCap,deltaCap,rCap,CrCap,ClCap,sig02
x0=np.array([[0],[0]])
A=np.array([[-1., 1.],
            [-1., 0.],
            [-1., 0.],
            [0., -1.],
            [0., -1.]])

W=np.array([[-L1],
            [H1-L2],
            [H2-L3],
            [H1-L4],
            [H2-L5]])

#Cr=np.array([[0.02**2,0,0,0,0],
#              [0,0.02**2,0,0,0],
#              [0,0,0.02**2,0,0],
#              [0,0,0,0.02**2,0],
#              [0,0,0,0,0.02**2]])

Cr=np.eye(5)*(0.02**2) 
# Cr matrisi bu şekilde olmak zorunda değil değişebilir ağırlıkları farklı olabilir

[xCap,CxCap,deltaCap,rCap,CrCap,ClCap,sig02]=EKK(A,W,Cr,x0)

print("x Cap:")
print(xCap)
print("Cx Cap:")
print(CxCap)
print("Delta Cap:")
print(deltaCap)
print("r Cap:")
print(rCap)
print("r Cap:")
print(rCap)
print("Cr Cap:")
print(CrCap)
print("Cl Cap:")
print(ClCap)
print("sig02 Cap:")
print(sig02)




