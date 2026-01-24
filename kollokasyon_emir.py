#!/usr/bin/env python3
# -- coding: utf-8 --
import numpy as np
import math
import matplotlib.pyplot as plt

# VERİLER
x01 = 0
x02 =  1.445
x03 =  2.890
x04 =  4.335
x05 =   5.780


y01 = 0.6108
y02 = 1.0863
y03 = 2.9034
y04 = 4.5925
y05 = 6.2714


C0 = 0.1260 # Kovaryansın başlangıç değeri veya maksimum değeri (örneğin, sinyal gücü)
a = 0.6 # Kovaryansın mesafeye (veya τ) göre ne kadar hızlı azaldığını belirleyen katsayıdır.Artırırsak Korelasyon hızlı değişeceği için diğer noktaları etkisi az olacaktır.
x0 = np.array([[0.6108], [0.3291]])
X = np.array([x01, x02, x03, x04, x05])
Y = np.array([y01, y02, y03, y04, y05])
print(x0[0], x0[1])

# W matrisi oluştururken Y değerlerini kullanılmasındaki sebep artık değerler olarak negatif ölçüleri kullanınca en büyük artık değeri verir.
# Yani bir nevi artıklıklarım başlangıç değeri olarak alıyoruz.
W = np.array([[0.6108+(0.3291*x01)-y01],
              [0.6108+(0.3291*x02)-y02],
              [0.6108+(0.3291*x03)-y03],
              [0.6108+(0.3291*x04)-y04],
              [0.6108+(0.3291*x05)-y05]
              ]) # Matematiksel işlemlerde kolaylık olsun diye y değerlerinin eksilisini alıyoruz.

print("W: \n", W, "\n")

# Y = a_0 + a_1 * x_1 +...+a_n * x_n
# Denklem bu olduğunda "a_0" offset değeri kaybolmasın diye ilk sütun 1 lerden oluşuyor.
A = np.array([[1, x01],
              [1, x02],
              [1, x03],
              [1, x04],
              [1, x05]
              ])

print("A: \n", A, "\n")

standart = 0.1**2
Cr = np.eye(5)*standart

print("Cr:\n", Cr, "\n")



# Varsayalım ki, standart sapma 50


CrInv = np.linalg.inv(Cr)

# Normal denklem
N = A.T @ CrInv @ A
deltaCap = -np.linalg.inv(N) @ A.T @ CrInv @ W
 
xCap=x0+deltaCap


print("A =\n", A)
print("W =\n", W)
print("N =\n", N)
print("Cr =\n", Cr)

# Çıktı: DeltaCap
print("DeltaCap Xcap:\n", deltaCap)

# CxCap hesaplaması
CxCap = np.linalg.inv(A.T @ CrInv @ A)
print("CxCap:\n", CxCap)

# RCap hesaplaması
rCap = A @ deltaCap + W
print("rCap:\n", rCap)

print("xCap\n", xCap)




# Çizim için veriler
x = np.array([x01, x02, x03, x04, x05])
y = np.array([y01, y02, y03, y04, y05])

# Doğru çizimi
a0 = deltaCap[0]
a1 = deltaCap[1]

xp = [x[0], x[4]]
yp = [a0 + a1 * x[0], a0 + a1 * x[4]]

plt.plot(xp, yp, label="Doğru", color="orange")
plt.scatter(x, y, color='red')  # Noktaları kırmızı ile göster

# Noktaları numaralandır
for i, (xi, yi) in enumerate(zip(x, y), start=1):
    plt.text(xi, yi, f"{i}", fontsize=10, ha='right', va='bottom')

plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Numaralandırılmış Noktalar ve Doğru")
plt.show()

print("B ŞIKKI KOLLAKASYON; \n")

Bv = -np.eye(5)
Bs = Bv


""" Cs nin oluşturulması """
def Kovaryans(xs,C0,a):
    n = len(xs)
    Cs = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            Tau = xs[j]-xs[i]
            Cs[i,j] = C0 * math.exp(-1*a*2*Tau*2)
    return Cs


""" Cs matrisi soncucu doğru """
Cs = Kovaryans(X,C0,a) # X veri seti için "C_0" başlangıç değeri ve "a" katsayısı ile tüm noktaların kendisi içerisindeki korelasyonunu inceler.

print("Cs:\n", Cs, "\n")


""" Buraya Dikkat Et """
Ms = Bs @ Cs @ Bs.T
Mv = Bv @ Cr @ Bv.T

print("Ms: \n", Ms, "\n")
print("Mv:\n", Mv, "\n")
""" M doğru sonuç """
M = np.linalg.inv(Cs + Cr) #Cr(ölçülerin hatasının diagonali) ile Cs'nin toplamı

print("M:\n", M, "\n")
""" N doğru sonuç """
N = np.linalg.inv(A.T @ M @ A) #Bilinmeyenlerin Kovaryans Matrisi

print("N:\n", N, "\n")

L = M - M @ A @ N @ A.T @ M

print("L:\n", L,"\n")

DeltaCap = -N @ A.T @ M @ W

print("deltaCap: \n", DeltaCap, "\n")

""" x0 = 0 # W yu hesaplarken 0 aldığımız için; """

XCap = x0 + DeltaCap

print("XCap: \n", XCap, "\n")

sCap =- Cs @ Bs.T @ L @ W #Ölçünün içindeki sinyalin değeri

print("sCap: \n", sCap, "\n")
# Standart sapma yüksek verildiği için rCap yüksek çıkıyor.Yoksa doğru.
rCap = -Cr @ Bv.T @ L @ W #Residual
print("rCap: \n", rCap, "\n")

P_üssü_f = (Y.T - rCap.T).T #10 + rCap

print("P^f : \n",P_üssü_f,"\n")