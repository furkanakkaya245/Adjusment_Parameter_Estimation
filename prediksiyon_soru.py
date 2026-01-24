import numpy as np
from paramDic_2 import Cr_, deltaCap_standart, xCap
import matplotlib.pyplot as plt

############################################ A

C0 = 1.20
a = 1e-5
sig_olcum = 10

x0 = np.array([-96.40, -81.13, -55.72, -29.12, -11.83,
                6.69, 37.58, 57.13, 74.11, 100.33])

y0 = np.array([-305.39, -205.59, -109.04, -30.26, -25.30,
                1.51, 92.71, 184.70, 214.84, 269.74])

A = np.column_stack((np.ones(len(x0)), x0))
W = -y0.reshape(-1,1)

Cr = Cr_(len(x0), sig_olcum)

x0_ = np.zeros((2,1))

deltaCap_ = deltaCap_standart(A, Cr, W)
xCap_ = xCap(x0_, deltaCap_)

print("deltaCap_a:\n", deltaCap_)
print("xCap_a:\n", xCap_)

# Çizim için veriler
x = np.array([x0[0], x0[1], x0[2], x0[3], x0[4], x0[5], x0[6], x0[7], x0[8], x0[9]])
y = np.array([y0[0], y0[1], y0[2], y0[3], y0[4], y0[5], y0[6], y0[7], y0[8], y0[9]])

# Doğru çizimi
a0 = deltaCap_[0]
a1 = deltaCap_[1]

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

###################################### B
Bv = -np.eye(10)
Bs = Bv

tao = np.array([
    [x0[0] - x0[0], x0[1] - x0[0], x0[2] - x0[0], x0[3] - x0[0], x0[4] - x0[0],x0[5] - x0[0],x0[6] - x0[0],x0[7] - x0[0],x0[8] - x0[0],x0[9] - x0[0]],
    [x0[0] - x0[1], x0[1] - x0[1], x0[2] - x0[1], x0[3] - x0[1], x0[4] - x0[1],x0[5] - x0[1],x0[6] - x0[1],x0[7] - x0[1],x0[8] - x0[1],x0[9] - x0[1]],
    [x0[0] - x0[2], x0[1] - x0[2], x0[2] - x0[2], x0[3] - x0[2], x0[4] - x0[2],x0[5] - x0[2],x0[6] - x0[2],x0[7] - x0[2],x0[8] - x0[2],x0[9] - x0[2]],
    [x0[0] - x0[3], x0[1] - x0[3], x0[2] - x0[3], x0[3] - x0[3], x0[4] - x0[3],x0[5] - x0[3],x0[6] - x0[3],x0[7] - x0[3],x0[8] - x0[3],x0[9] - x0[3]],
    [x0[0] - x0[4], x0[1] - x0[4], x0[2] - x0[4], x0[3] - x0[4], x0[4] - x0[4],x0[5] - x0[4],x0[6] - x0[4],x0[7] - x0[4],x0[8] - x0[4],x0[9] - x0[4]],
    [x0[0] - x0[5], x0[1] - x0[5], x0[2] - x0[5], x0[3] - x0[5], x0[4] - x0[5],x0[5] - x0[5],x0[6] - x0[5],x0[7] - x0[5],x0[8] - x0[5],x0[9] - x0[5]],
    [x0[0] - x0[6], x0[1] - x0[6], x0[2] - x0[6], x0[3] - x0[6], x0[4] - x0[6],x0[5] - x0[6],x0[6] - x0[6],x0[7] - x0[6],x0[8] - x0[6],x0[9] - x0[6]],
    [x0[0] - x0[7], x0[1] - x0[7], x0[2] - x0[7], x0[3] - x0[7], x0[4] - x0[7],x0[5] - x0[7],x0[6] - x0[7],x0[7] - x0[7],x0[8] - x0[7],x0[9] - x0[7]],
    [x0[0] - x0[8], x0[1] - x0[8], x0[2] - x0[8], x0[3] - x0[8], x0[4] - x0[8],x0[5] - x0[8],x0[6] - x0[8],x0[7] - x0[8],x0[8] - x0[8],x0[9] - x0[8]],
    [x0[0] - x0[9], x0[1] - x0[9], x0[2] - x0[9], x0[3] - x0[9], x0[4] - x0[9],x0[5] - x0[9],x0[6] - x0[9],x0[7] - x0[9],x0[8] - x0[9],x0[9] - x0[9]],
])

# Cs = C0 * np.exp(-(a) * (tao ** 2))  

def Kovaryans(xs,C0,a):
    n = len(xs)
    Cs = np.zeros([n,n])
    for i in range(n):
        for j in range(n):
            Tau = xs[j]-xs[i]
            Cs[i,j] = C0 * np.exp(-1*a*(Tau**2))
    return Cs
Cs=Kovaryans(x0,C0,a)
print(f"Cs:\n{Cs}")

Cr = np.eye(10)*0.01
M = np.linalg.inv(Cr + Cs)
A = np.array([[1, x] for x in x0])
N = np.linalg.inv(A.T@M@A)
L = M-M@A@N@A.T@M
deltaCap2 = -N@A.T@M@W
xCap_b=xCap(x0_,deltaCap2)
print(f"\ndeltaCap_b:\n{deltaCap2}")
print(f"xCap_b:\n{xCap_b}\n")
