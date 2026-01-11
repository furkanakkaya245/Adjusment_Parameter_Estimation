import numpy as np
from paramDic_2 import deltaCap_standart, xCap, kosullu_deltaCap, Cr_
import matplotlib.pyplot as plt
x01= -91.45
y01= -143.69
x02= -88.61
y02= -181.17
x03= -81.94
y03= -64.09
x04= -59.19
y04=  1.88
x05=  -16
y05=  68.07
x06= -0.43
y06= 104.92
x07= 26.17
y07= 136.93
x08= 50.45
y08= 203.98
x09= 69.57
y09= 210.28
x10= 97.41
y10= 341.71

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
sig=150
Cr=Cr_(10,sig)
deltaCap_Normal=deltaCap_standart(A,Cr,W)
xCap_Normal=xCap(x0,deltaCap_Normal)
print(f"deltaCap_Normal:\n{deltaCap_Normal}\nxCap_Normal:\n{xCap_Normal}\n")

# Doğrunun 5 numaralı noktadan geçitği koşulun işlenmesi
x = np.array([x01, x02, x03, x04, x05, x06, x07, x08, x09, x10])
y = np.array([y01, y02, y03, y04, y05, y06, y07, y08, y09, y10])
Ac = np.array([[1, x[4]]])  
Wc = np.array([-y[4]])
x0_c = [[0],[0]]

deltaCap_Kosul_1=kosullu_deltaCap(A,Ac,W,Wc,Cr,10,sig)
xCap_Kosul_1=xCap(x0_c,deltaCap_Kosul_1)
print(f"deltaCap_Kosul_1:\n{deltaCap_Kosul_1}\nxCap_kosul_1:\n{xCap_Kosul_1}\n")

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





