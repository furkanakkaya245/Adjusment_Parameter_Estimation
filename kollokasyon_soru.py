#!/usr/bin/env python3
# -- coding: utf-8 --


import numpy as np
import math
import matplotlib.pyplot as plt



""" deltakep xcap rcap doğru sonuç veriyor """
# VERİLER
x01 = -96.40
x02 =  -81.13
x03 =  -55.72
x04 =  -29.12
x05 =   -11.83
x06 =  6.69
x07 =  37.58
x08 =  57.13
x09 =  74.11
x10 =   100.33


y01 = -305.39
y02 = -205.59
y03 = -109.04
y04 = -30.26
y05 = -25.30
y06 = 1.51
y07 = 92.71
y08 = 184.70
y09 = 214.84
y10 = 269.74


C0 = 45.465591395093156 # Kovaryansın başlangıç değeri veya maksimum değeri (örneğin, sinyal gücü)
a = 1.0 # Kovaryansın mesafeye (veya τ) göre ne kadar hızlı azaldığını belirleyen katsayıdır.Artırırsak Korelasyon hızlı değişeceği için diğer noktaları etkisi az olacaktır.
x0 = np.array([[0.0], [0.0]])
X = np.array([x01, x02, x03, x04, x05,x06, x07, x08, x09, x10])
Y = np.array([y01, y02, y03, y04, y05,y06, y07, y08, y09, y10])
print(x0[0], x0[1])

# W matrisi oluştururken Y değerlerini kullanılmasındaki sebep artık değerler olarak negatif ölçüleri kullanınca en büyük artık değeri verir.
# Yani bir nevi artıklıklarım başlangıç değeri olarak alıyoruz.
W = np.array([[-y01],
              [-y02],
              [-y03],
              [-y04],
              [-y05],
              [-y06],
              [-y07],
              [-y08],
              [-y09],
              [-y10]
              ]) # Matematiksel işlemlerde kolaylık olsun diye y değerlerinin eksilisini alıyoruz.

print("W: \n", W, "\n")

# Y = a_0 + a_1 * x_1 +...+a_n * x_n
# Denklem bu olduğunda "a_0" offset değeri kaybolmasın diye ilk sütun 1 lerden oluşuyor.
A = np.array([[1, x01],
              [1, x02],
              [1, x03],
              [1, x04],
              [1, x05],
              [1, x06],
              [1, x07],
              [1, x08],
              [1, x09],
              [1, x10]
              ])

print("A: \n", A, "\n")

standart = 10**2
Cr = np.eye(10)*standart

print("Cr:\n", Cr, "\n")



# Varsayalım ki, standart sapma 50
print("NORMAL EKK ÇÖZÜMÜ \n")

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
x = np.array([x01, x02, x03, x04, x05,x06, x07, x08, x09, x10])
y = np.array([y01, y02, y03, y04, y05,y06, y07, y08, y09, y10])

# Doğru çizimi
a0 = deltaCap[0]
a1 = deltaCap[1]

xp = [x[0], x[9]]
yp = [a0 + a1 * x[0], a0 + a1 * x[9]]

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

Bv = -np.eye(10)
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
rCap2 = -Cr@np.linalg.inv(Cs+Cr)@Y
print("rCap: \n", rCap, "\n")


P_üssü_f = (Y.T - rCap.T).T #10 + rCap

print("P^f : \n",P_üssü_f,"\n")





#C ŞIKKI C0 = 100 a =2 ye göre çözüm
C01 = 100 # Kovaryansın başlangıç değeri veya maksimum değeri (örneğin, sinyal gücü)
a1 = 2 # Kovaryansın mesafeye (veya τ) göre ne kadar hızlı azaldığını belirleyen katsayıdır.Artırırsak Korelasyon hızlı değişeceği için diğer noktaları etkisi az olacaktır.
Bv = -np.eye(10)
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
Cs1 = Kovaryans(X,C01,a1) # X veri seti için "C_0" başlangıç değeri ve "a" katsayısı ile tüm noktaların kendisi içerisindeki korelasyonunu inceler.


print("C ŞIKKI ÇÖZÜMÜ \n")
print("Cs:\n", Cs1, "\n")


""" Buraya Dikkat Et """
Ms = Bs @ Cs1 @ Bs.T
Mv = Bv @ Cr @ Bv.T

print("Ms: \n", Ms, "\n")
print("Mv:\n", Mv, "\n")
""" M doğru sonuç """
M = np.linalg.inv(Cs1 + Cr) #Cr(ölçülerin hatasının diagonali) ile Cs'nin toplamı

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

sCap =Cs1@L@W #Ölçünün içindeki sinyalin değeri

print("sCap: \n", sCap, "\n")
# Standart sapma yüksek verildiği için rCap yüksek çıkıyor.Yoksa doğru.
rCap = -Cr @ Bv.T @ L @ W #Residual
rCap2 = -Cr@np.linalg.inv(Cs1+Cr)@Y
print("rCap: \n", rCap, "\n")


P_üssü_f = (Y.T - rCap.T).T #10 + rCap

print("P^f : \n",P_üssü_f,"\n")