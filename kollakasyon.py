import numpy as np
from paramDic_2 import kollakasyon,Cr_



a0=np.array([[0],
             [1.445],
             [2.890],
             [4.335],
             [5.780]])
a1=np.array([[0.6108],
             [1.0863],
             [2.9034],
             [4.5925],
             [6.2714]])
x1_0=0.6108
x2_0=0.3291
x0=np.array([[x1_0],
             [x2_0]])
A= np.array([[1, a0[0][0]],  
                          [1, a0[1][0]],
                          [1, a0[2][0]],
                          [1, a0[3][0]],
                          [1, a0[4][0]]
                         ])
W = x1_0 + (x2_0 * a0) - a1

print(f"A:\n{A}\nW:\n{W}\n")
T=np.eye(5)


sonuc=kollakasyon(5,0.01,A,W,0.1260,T,a0,0.6).sonuc()
print(x0+sonuc[0])
