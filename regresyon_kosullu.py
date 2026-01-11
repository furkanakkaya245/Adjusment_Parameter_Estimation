import numpy as np
import matplotlib.pyplot as plt
from paramDic_2 import dms_to_radian
from paramDic_2 import deltaCap_Bayesian
# Başlangıç değerleri
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

# Y = A * X denklemi
A = np.array([[1, x01], [1, x02], [1, x03], [1, x04], [1, x05], [1, x06], [1, x07], [1, x08], [1, x09], [1, x10]])
W = np.array([[-y01], [-y02], [-y03], [-y04], [-y05], [-y06], [-y07], [-y08], [-y09], [-y10]])

# Varsayalım ki, standart sapma 50
standart = 150**2
# 10 tane ölçü var
Cr = np.eye(10) * standart
CrInv = np.linalg.inv(Cr)

# Normal denklem
# yaklaşık değerleri 0 aldık. y = ax + b 'deki a ve b bilinmeyenler
x0 = [[0],[0]]
N = A.T @ CrInv @ A
deltaCap = -np.linalg.inv(N) @ A.T @ CrInv @ W
xCap = x0 + deltaCap

# Çıktı: DeltaCap
print(f"DeltaCap:\n{deltaCap}\nxCap:\n{xCap}")

# CxCap hesaplaması
CxCap = np.linalg.inv(A.T @ CrInv @ A)
# print("CxCap:", CxCap)

# RCap hesaplaması
rCap = A @ deltaCap + W
# print("rCap:", rCap)

# Çizim için veriler
x = np.array([x01, x02, x03, x04, x05, x06, x07, x08, x09, x10])
y = np.array([y01, y02, y03, y04, y05, y06, y07, y08, y09, y10])

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
plt.title("EKK Numaralandırılmış Noktalar ve Doğru")
plt.show()
##########################################################################################################
# KOŞULLU ÇÖZÜM : 5. noktanın üzerinden geçecek doğru
AC = np.array([[1, x[4]]])  # 5. nokta (index 4)
WC = np.array([-y[4]])
x0_c = [[0],[0]]

deltaCap2 = deltaCap - np.linalg.inv(N) @ AC.T @ np.linalg.inv(AC @ np.linalg.inv(N) @ AC.T) @ (WC + AC @ deltaCap)
xCap2 = x0_c + deltaCap2


print(f"Ac:\n{AC}\nWc:\n{WC}")
print(f"DeltaCap_Kosul:\n{deltaCap2}\nxCap_Kosul:\n{xCap2}\n")

# Yeni doğru çizimi
# 10 ölçü var, 0 ve 9 arasında değer alacak.
xp2 = [x[0], x[9]]
yp2 = [deltaCap2[0] + deltaCap2[1] * x[0], deltaCap2[0] + deltaCap2[1] * x[9]]

plt.plot(xp2, yp2, color="green", label="Yeni Doğru")
plt.scatter(x, y, color="blue")  # Yeni noktalar

# Noktaları numaralandır
for i, (xi, yi) in enumerate(zip(x, y), start=1):
    plt.text(xi, yi, f"{i}", fontsize=10, ha='right', va='bottom')

plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("(Koşullu)Numaralandırılmış Noktalar ve Yeni Doğru (5. nokta)")
plt.show()


##########################################################################################################
# KOŞULLU ÇÖZÜM : eğimi 70 olan doğru
egim=dms_to_radian(70,0,0)
egimtan=np.tan(egim)
AC = np.array([[0,1]])  
WC = np.array([-egimtan])
x0_c = [[0],[0]]

deltaCap2 = deltaCap - np.linalg.inv(N) @ AC.T @ np.linalg.inv(AC @ np.linalg.inv(N) @ AC.T) @ (WC + AC @ deltaCap)
xCap2 = x0_c + deltaCap2


print(f"Ac:\n{AC}\nWc:\n{WC}")
print(f"DeltaCap_Kosul_egim:\n{deltaCap2}\nxCap_Kosul_egim:\n{xCap2}\n")

xp2 = [x[0], x[9]]
yp2 = [deltaCap2[0] + deltaCap2[1] * x[0], deltaCap2[0] + deltaCap2[1] * x[9]]

plt.plot(xp2, yp2, color="green", label="Yeni Doğru egim")
plt.scatter(x, y, color="blue")  # Yeni noktalar

# Noktaları numaralandır
for i, (xi, yi) in enumerate(zip(x, y), start=1):
    plt.text(xi, yi, f"{i}", fontsize=10, ha='right', va='bottom')

plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("(Koşullu)Numaralandırılmış Noktalar ve Yeni Doğru (Eğim)")
plt.show()
##########################################################################################################
# KOŞULLU ÇÖZÜM : hem 1 hem 5 ten geçecek şekilde
AC = np.array([[1, x[0]],
               [1, x[4]]])  # 5. nokta (index 4)
WC = np.array([[-y[0]],
               [-y[4]]])
x0_c = [[0],[0]]

deltaCap2 = deltaCap - np.linalg.inv(N) @ AC.T @ np.linalg.inv(AC @ np.linalg.inv(N) @ AC.T) @ (WC + AC @ deltaCap)
xCap2 = x0_c + deltaCap2


print(f"Ac:\n{AC}\nWc:\n{WC}")
print(f"DeltaCap_Kosul:\n{deltaCap2}\nxCap_Kosul:\n{xCap2}\n")

# Yeni doğru çizimi
# 10 ölçü var, 0 ve 9 arasında değer alacak.
xp2 = [x[0], x[9]]
yp2 = [deltaCap2[0] + deltaCap2[1] * x[0], deltaCap2[0] + deltaCap2[1] * x[9]]

plt.plot(xp2, yp2, color="green", label="Yeni Doğru")
plt.scatter(x, y, color="blue")  # Yeni noktalar

# Noktaları numaralandır
for i, (xi, yi) in enumerate(zip(x, y), start=1):
    plt.text(xi, yi, f"{i}", fontsize=10, ha='right', va='bottom')

plt.legend()
plt.xlabel("X")
plt.ylabel("Y")
plt.title("(Koşullu)Numaralandırılmış Noktalar ve Yeni Doğru (1-5) Noktaları")
plt.show()





