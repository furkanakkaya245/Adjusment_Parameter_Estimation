import numpy as np
from numpy.linalg import inv
import math

def EKK(A,W,Cr,x0,l0,n,u):
    N=A.T@inv(Cr)@A
    CrInv = np.linalg.inv(Cr)
    CxCap = inv(N)
    deltaCap = -1*CxCap@A.T@CrInv@W
    xCap = x0 + deltaCap
    rCap = A@deltaCap+W
    lCap=l0+rCap
    CrCap=Cr-(A@inv(N)@A.T)
    ClCap=Cr-CrCap
    sig2=(rCap.T@inv(Cr)@rCap)/(n-u)
    
    return xCap,CxCap,deltaCap,rCap,sig2,ClCap,CrCap,lCap

def dms_to_degree(derece, dakika=0, saniye=0):
    # DMS → Decimal derece
    decimal_degree = derece + dakika / 60 + saniye / 3600
    # Decimal derece → Radyan
    radian = math.radians(decimal_degree)
    return radian
