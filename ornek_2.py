import numpy as np
from numpy.linalg import inv
import paramDic_2
# Ölçüler
L1= 131.02
L2= 52.49
L3= 257.50
L4= -78.53
L5= 126.48
L6= 205.01
# Ölçü hata
sig=0.02
# Bilinen Değerler
P1_0= 88.52
P2_0= 220.73
P3_0= 141.50
P4_0= 347.11
# Bilinen Değer Hata
P_hata=1

A=np.array([[-1,1,0,0],
            [-1,0,1,0],
            [-1,0,0,1],
            [0,-1,1,0],
            [0,-1,0,1],
            [0,0,-1,1]
            ])
x0=np.array([[0],
             [0],
             [0],
             [0]])
x0_=np.array([[P1_0],
             [P2_0],
             [P3_0],
             [P4_0]])
l0=np.array([[L1],
             [L2],
             [L3],
             [L4],
             [L5],
             [L6]])
# Bilinmeyenler Hakkında Önceden Bilgi Olmadan Çözüm
W=(A@x0)-l0
Cr=paramDic_2.Cr_(6,sig)
#deltaCap_normal=paramDic_2.deltaCap_standart(A,Cr,W)
#xCap_normal=paramDic_2.xCap(x0,deltaCap_normal)
# Bilinmeyenler Hakkında Önceden Bilgi Kullanılırak Çözüm
W_=(A@x0_)-l0
Cr=paramDic_2.Cr_(6,sig)
C0=paramDic_2.C0(4,P_hata)
deltaCap_bayes=paramDic_2.deltaCap_Bayesian(A,Cr,W_,C0)
xCap_bayes=paramDic_2.xCap(x0_,deltaCap_bayes)

#print(f"Bilgi kullanılmadan Sonuclar................\nDeltaCap:\n{deltaCap_normal}\nxCap:\n{xCap_normal}")
print(f"Bilgi kullanılarak Sonuclar................\nDeltaCap:\n{deltaCap_bayes}\nxCap:\n{xCap_bayes}")


