import numpy as np
import matplotlib.pyplot as plt
from paramDic_2 import Kollokasyon, deltaCap_standart, Cr_,xCap, CxCap_, rCap_

# 1. VERİ GİRİŞİ 
x_val = [ -94.40,
          -81.13,
          -55.72,
          -29.12,
          -11.83,
            6.69,
           37.58,
           57.13,
           74.11,
          100.33]

y_val = [ -305.39,
          -205.59,
          -109.04,
          -30.26,
          -25.30,
            1.51,
           92.71,
           184.70,
           214.84,
          269.74]
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
C0= 45.465591395093156
a= 1.0
x_val = np.array([ [-94.40],
          [-81.13],
          [-55.72],
          [-29.12],
          [-11.83],
            [6.69],
           [37.58],
           [57.13],
           [74.11],
          [100.33]])
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


# C ŞIKKI:
C0= 100 
a= 2.0
x_val = np.array([ [-94.40],
          [-81.13],
          [-55.72],
          [-29.12],
          [-11.83],
            [6.69],
           [37.58],
           [57.13],
           [74.11],
          [100.33]])
cozum_C=Kollokasyon(x_val)
xCap_c, deltaCap_c, sCap_c, rCap_c, M_c, N_c, L_mat_c, Cs_c, Cr_c, y_total_c=cozum_C.hesapla( W, x0, C0, a, sig)
print("\nC ŞIKKI SONUÇLARI:\n")
print("DeltaCap:\n", deltaCap_c)
print("CxCap =\n", sCap_c)
print("rCap:\n", rCap_c)
print("xCap\n", xCap_c)
print("M Matrisi:\n", M_c)
print("N Matrisi:\n", N_c)
print("L Matrisi:\n", L_mat_c)
print("Cs Matrisi:\n", Cs_c)
print("Cr Matrisi:\n", Cr_c)
print("y_total:\n", y_total_c)

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
# C Şıkkı: Kollokasyon 2 
y_total_c = np.array(y_total_c).flatten()
plt.plot(x_val, y_total_c, color='purple', marker='x', linestyle=':', linewidth=2, label='Kollokasyon_c (C0=100, a=2)')
plt.title("Kollokasyon vs EKK Karşılaştırması", fontsize=16)
plt.xlabel("Konum (x)", fontsize=12)
plt.ylabel("Değer (y)", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, linestyle=':', alpha=0.6)
for i in range(len(x_val)):
    plt.plot([x_val[i], x_val[i]], [y_val[i], y_trend[i]], color='gray', linestyle='-', alpha=0.3)
plt.show()
