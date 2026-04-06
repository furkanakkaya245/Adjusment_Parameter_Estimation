import numpy as np
from paramDic_2 import deltaCap_standart, xCap, kosullu_deltaCap, Cr_
import matplotlib.pyplot as plt
x01= -68.51
y01= -39.40
x02= -1.06
y02= 66.92
x03= -1.01
y03= 51.92
x04= 4.02
y04= 59.46
x05= 20.47
y05= 122.67
x06= 45.87
y06= 135.04
x07= 46.11
y07= 125.91
x08= 79.83
y08= 178.09
x09= 82.12
y09= 215.96
x10= 93.02
y10= 225.98

A = np.array([[1, x01], 
              [1, x02], 
              [1, x03], 
              [1, x04], 
              [1, x05], 
              [1, x06], 
              [1, x07], 
              [1, x08], 
              [1, x09], 
              [1, x10]])
W = np.array([[-y01], 
              [-y02], 
              [-y03], 
              [-y04], 
              [-y05], 
              [-y06], 
              [-y07], 
              [-y08], 
              [-y09], 
              [-y10]])
x0=np.array([[0],
             [0]])
sig=50
Cr=Cr_(10,sig)
deltaCap_Normal=deltaCap_standart(A,Cr,W)
xCap_Normal=xCap(x0,deltaCap_Normal)
print(f"deltaCap_Normal:\n{deltaCap_Normal}\nxCap_Normal:\n{xCap_Normal}\n")

# Doğrunun 6 numaralı noktadan geçitği koşulun işlenmesi
x = np.array([x01, x02, x03, x04, x05, x06, x07, x08, x09, x10])
y = np.array([y01, y02, y03, y04, y05, y06, y07, y08, y09, y10])
Ac = np.array([[1, x[5]]])  
Wc = np.array([-y[5]])
x0_c = [[0],[0]]

deltaCap_Kosul_1=kosullu_deltaCap(A,Ac,W,Wc,Cr,10,sig)
xCap_Kosul_1=xCap(x0_c,deltaCap_Kosul_1)
print(f"deltaCap_Kosul_1:\n{deltaCap_Kosul_1}\nxCap_kosul_1:\n{xCap_Kosul_1}\n")
# çizim
xp2 = [x[0], x[9]]
yp2 = [deltaCap_Normal[0] + deltaCap_Normal[1] * x[0], deltaCap_Normal[0] + deltaCap_Normal[1] * x[9]]
plt.plot(xp2, yp2, color="green", label="Yeni Doğru")
plt.scatter(x, y, color="blue")  # Yeni noktalar
# Noktaları numaralandır
for i, (xi, yi) in enumerate(zip(x, y), start=1):
    plt.text(xi, yi, f"{i}", fontsize=10, ha='right', va='bottom')
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Normal Doğru")
plt.show()

xp2 = [x[0], x[9]]
yp2 = [deltaCap_Kosul_1[0] + deltaCap_Kosul_1[1] * x[0], deltaCap_Kosul_1[0] + deltaCap_Kosul_1[1] * x[9]]
plt.plot(xp2, yp2, color="green", label="Yeni Doğru")
plt.scatter(x, y, color="blue")  # Yeni noktalar
# Noktaları numaralandır
for i, (xi, yi) in enumerate(zip(x, y), start=1):
    plt.text(xi, yi, f"{i}", fontsize=10, ha='right', va='bottom')
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("(Koşullu)Yeni Doğru")
plt.show()





