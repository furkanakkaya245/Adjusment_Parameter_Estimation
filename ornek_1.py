import numpy as np
from numpy.linalg import inv
from paramDic_2 import deltaCap_standart, deltaCap_Bayesian, xCap, Cr_,C0

H1= 126.20
L1= -142.41
L2= 85.05
L3= -136.75
L4= 227.45
L5= 5.66
L6= -221.79
sig=0.02
P1_0= 261.48
P2_0= 121.52
P3_0= 348.45
P_Hata= 1

# Bilinmeyenler Hakkında Bilgi Kullanmadan

A=np.array([[-1,1,0],
            [-1,0,1],
            [-1,0,0],
            [0,-1,1],
            [0,-1,0],
            [0,0,-1]
            ])
x0=np.array([[0],
             [0],
             [0]])
W=np.array([[-L1],
             [-L2],
             [H1-L3],
             [-L4],
             [H1-L5],
             [H1-L6]])
l0=np.array([[L1],
             [L2],
             [L3],
             [L4],
             [L5],
             [L6]])
Cr=Cr_(6,sig)
N=A.T@inv(Cr)@A
deltaCap=deltaCap_standart(A,Cr,W)
xCap_=xCap(x0,deltaCap)
print(f"A Şıkkı=\ndeltaCap_A:\n{deltaCap}\nxCap_A:\n{xCap_}\n")

# Bilinmeyenler Hakkında Bilgi Kullanarak

x0_ek=np.array([[P1_0],
             [P2_0],
             [P3_0]])
C_x0=C0(3,P_Hata)
W_yeni=(A@x0_ek)+W

deltaCap_ek=deltaCap_Bayesian(A,Cr,W_yeni,C_x0)
xCap_ek=xCap(x0_ek,deltaCap_ek)
print(f"B Şıkkı=\ndeltaCap_B:\n{deltaCap_ek}\nxCap_B:\n{xCap_ek}\n")


# Sadece P1 noktasına ilişkin bilgiyi kullanarak çözüm

x0_ek_p1=np.array([[P1_0],
             [0],
             [0]])
C_x0_p1=C0(3,P_Hata)
C_x0_p1[0,0]=1**2
C_x0_p1[1,1]=1000000000**2
C_x0_p1[2,2]=1000000000**2
W_yeni=(A@x0_ek_p1)+W
deltaCap_ek_p1=deltaCap_Bayesian(A,Cr,W_yeni,C_x0_p1)
xCap_ek_p1=xCap(x0_ek_p1,deltaCap_ek_p1)
print(f"C Şıkkı=\ndeltaCap_C:\n{deltaCap_ek_p1}\nxCap_C:\n{xCap_ek_p1}\n")

# h1', bilinmeyen olarak alırsak
H1_hata=0.05
A_h1=np.array([[-1,1,0,0],
            [-1,0,1,0],
            [-1,0,0,1],
            [0,-1,1,0],
            [0,-1,0,1],
            [0,0,-1,1]
            ])
x0_ek_h1=np.array([[P1_0],
             [P2_0],
             [P3_0],
             [H1]])
W_h1=np.array([[-L1],
             [-L2],
             [-L3],
             [-L4],
             [-L5],
             [-L6]])
l0=np.array([[L1],
             [L2],
             [L3],
             [L4],
             [L5],
             [L6]])
Cr=Cr_(6,sig)
C_x0_h1=C0(4,P_Hata)
C_x0_h1[3,3]=H1_hata**2
W_yeni_h1=(A_h1@x0_ek_h1)+W_h1
deltaCap_ek_h1=deltaCap_Bayesian(A_h1,Cr,W_yeni_h1,C_x0_h1)
xCap_ek_h1=xCap(x0_ek_h1,deltaCap_ek_h1)
print(f"E Şıkkı=\ndeltaCap_E:\n{deltaCap_ek_h1}\nxCap_E:\n{xCap_ek_h1}\n")

# H1'in yüksekliğinin hatalı olarak 136.2 alındığı çözüm
H1_hata=0.05
H1=136.2
A_h1=np.array([[-1,1,0,0],
            [-1,0,1,0],
            [-1,0,0,1],
            [0,-1,1,0],
            [0,-1,0,1],
            [0,0,-1,1]
            ])
x0_ek_h1=np.array([[P1_0],
             [P2_0],
             [P3_0],
             [H1]])
W_h1=np.array([[-L1],
             [-L2],
             [-L3],
             [-L4],
             [-L5],
             [-L6]])

l0=np.array([[L1],
             [L2],
             [L3],
             [L4],
             [L5],
             [L6]])
Cr=Cr_(6,sig)
C_x0_h1=np.eye(4)*(P_Hata**2)
C_x0_h1[3,3]=H1_hata**2
W_yeni_h1=(A_h1@x0_ek_h1)+W_h1
deltaCap_ek_h1_farklı=deltaCap_Bayesian(A_h1,Cr,W_yeni_h1,C_x0_h1)
xCap_ek_h1=xCap(x0_ek_h1,deltaCap_ek_h1)
print(f"F Şıkkı=\ndeltaCap_F:\n{deltaCap_ek_h1_farklı}\nxCap_F:\n{xCap_ek_h1}\n")

# L6 ölçüsünü -225.0 alındığındaki çözüm
H1_hata=0.05
H1=136.2
A_h1=np.array([[-1,1,0,0],
            [-1,0,1,0],
            [-1,0,0,1],
            [0,-1,1,0],
            [0,-1,0,1],
            [0,0,-1,1]
            ])
x0_ek_h1=np.array([[P1_0],
             [P2_0],
             [P3_0],
             [H1]])
W_h1=np.array([[-L1],
             [-L2],
             [-L3],
             [-L4],
             [-L5],
             [-(-225.0)]])

l0=np.array([[L1],
             [L2],
             [L3],
             [L4],
             [L5],
             [L6]])
Cr=Cr_(6,sig)
C_x0_h1=np.eye(4)*(P_Hata**2)
C_x0_h1[3,3]=H1_hata**2
W_yeni_h1=(A_h1@x0_ek_h1)+W_h1
deltaCap_ek_h1_l6=deltaCap_Bayesian(A_h1,Cr,W_yeni_h1,C_x0_h1)
xCap_ek_h1=xCap(x0_ek_h1,deltaCap_ek_h1_l6)
print(f"G Şıkkı=\ndeltaCap_G:\n{deltaCap_ek_h1_l6}\nxCap_G:\n{xCap_ek_h1}\n")









