import numpy as np
from paramDic_2 import Cr_, deltaCap_standart, xCap,Prediksiyon,Kollokasyon,rCap_,CxCap_
import matplotlib.pyplot as plt
sig= 10
x0 = np.array([-96.40, -81.13, -55.72, -29.12, -11.83,
                6.69, 37.58, 57.13, 74.11, 100.33])
y0 = np.array([-305.39, -205.59, -109.04, -30.26, -25.30,
                1.51, 92.71, 184.70, 214.84, 269.74])

A = np.array([[1, x0[0]],
              [1, x0[1]],
              [1, x0[2]],
              [1, x0[3]],
              [1, x0[4]],
              [1, x0[5]],
              [1, x0[6]],
              [1, x0[7]],
              [1, x0[8]],
              [1, x0[9]] 
              ])
W= np.array([[-y0[0]],
              [-y0[1]],
              [-y0[2]],
              [-y0[3]],
              [-y0[4]],
              [-y0[5]],
              [-y0[6]],
              [-y0[7]],
              [-y0[8]],
              [-y0[9]]
              ])
Cr = Cr_(10,sig)
deltaCap_a= deltaCap_standart(A,Cr,W)
CxCap_a= CxCap_(A, Cr)
rCap_a= rCap_(A, deltaCap_a, W)
xCap_a=xCap(x0,deltaCap_a)
print("A =\n", A)
print("W =\n", W)
print("Cr =\n", Cr)
print("DeltaCap:\n", deltaCap_a)
print("CxCap =\n", CxCap_a)
print("rCap:\n", rCap_a)
print("xCap\n", xCap_a)
# Kollokasyon
C0 = 1.20
a = 1e-5
x0_ = np.array([[x0[0]],
              [x0[1]],
              [x0[2]],
              [x0[3]],
              [x0[4]],
              [x0[5]],
              [x0[6]],
              [x0[7]],
              [x0[8]],
              [x0[9]] 
              ])
kollokasyon=Kollokasyon(x0_)
cozum_kollokasyon=kollokasyon.hesapla(W, np.array([0, 0]), C0, a, sig)
print("Kollokasyon Çözümü:\n")
print("deltaCap:\n", cozum_kollokasyon[1])
print("xCap:\n", cozum_kollokasyon[0])
print("sCap:\n", cozum_kollokasyon[2])
print("rCap:\n", cozum_kollokasyon[3])
print("Cs:\n", cozum_kollokasyon[7])
print("Cr:\n", cozum_kollokasyon[8])
print("W:\n", cozum_kollokasyon[9])
