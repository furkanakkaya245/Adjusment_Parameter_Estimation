import numpy as np
import matplotlib.pyplot as plt
from paramDic_2 import Kollokasyon, deltaCap_standart, Cr_,xCap, CxCap_, rCap_

# 1. VERİ GİRİŞİ 
x_val = [ -103.47,
          -79.75,
          -59.94,
          -33.73,
          -7.76,
          15.38,
          35.60,
           58.24,
           75.47,
          101.44]

y_val = [ -257.83,
          -266.19,
          -113.06,
          -33.56,
          47.65,
            71.64,
           178.57,
           245.17,
           218.30,
          372.36]
sig = 10

# A ŞIKKI: EKK ÇÖZÜMÜ 
print("\nA ŞIKKI SONUÇLARI:\n")
A = np.array([[1, x_val[0]],
              [1, x_val[1]],
              [1, x_val[2]],
              [1, x_val[3]],
              [1, x_val[4]],
              [1, x_val[5]],
              [1, x_val[6]],
              [1, x_val[7]],
              [1, x_val[8]],
              [1, x_val[9]] 
              ])
W= np.array([[-y_val[0]],
              [-y_val[1]],
              [-y_val[2]],
              [-y_val[3]],
              [-y_val[4]],
              [-y_val[5]],
              [-y_val[6]],
              [-y_val[7]],
              [-y_val[8]],
              [-y_val[9]]
              ])
x0= np.array([[0],
              [0]
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
# B ŞIKKI: KOLLOKASYON ÇÖZÜMÜ
C0= 28.870253065261615
a= 1.0
x_val = np.array([ [x_val[0]],
                   [x_val[1]],
                   [x_val[2]],
                   [x_val[3]],
                   [x_val[4]],
                   [x_val[5]],
                   [x_val[6]],
                   [x_val[7]],
                   [x_val[8]],
                   [x_val[9]]])
cozum_B=Kollokasyon(x_val)
xCap_b, deltaCap_b, sCap_b, rCap_b, M_b, N_b, L_mat_b, Cs_b, Cr_b, y_total_b=cozum_B.hesapla( W, x0, C0, a, sig)
print("\nB ŞIKKI SONUÇLARI:\n")
print("DeltaCap:\n", deltaCap_b)
print("CxCap =\n", sCap_b)
print("rCap:\n", rCap_b)
print("xCap\n", xCap_b)
print("M Matrisi:\n", M_b)
print("N Matrisi:\n", N_b)
print("L Matrisi:\n", L_mat_b)
print("Cs Matrisi:\n", Cs_b)
print("Cr Matrisi:\n", Cr_b)
print("y_total:\n", y_total_b)

plt.figure(figsize=(12, 8))
# 1. Orijinal Ölçüler
# x_val ve y_val'in numpy array olduğundan emin olalım (Garanti olsun)
x_val = np.array(x_val).flatten()
y_val = np.array(y_val).flatten()
plt.scatter(x_val, y_val, color='red', s=80, label='Ölçülen Değerler', zorder=5)
# A Şıkkı: EKK Doğrusu
a0 = float(xCap_a[0])
a1 = float(xCap_a[1]) 
y_trend = a0 + a1 * x_val
plt.plot(x_val, y_trend, color='blue', linestyle='--', linewidth=2, label='EKK (Trend)')
# B Şıkkı: Kollokasyon 1
y_total_b = np.array(y_total_b).flatten()
plt.plot(x_val, y_total_b, color='green', marker='o', linestyle='-', alpha=0.7, label='Kollokasyon_b (C0=45, a=1)')

plt.title("Kollokasyon vs EKK Karşılaştırması", fontsize=16)
plt.xlabel("Konum (x)", fontsize=12)
plt.ylabel("Değer (y)", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
for i in range(len(x_val)):
    plt.plot([x_val[i], x_val[i]], [y_val[i], y_trend[i]], color='gray', linestyle='-', alpha=0.3)
plt.show()
