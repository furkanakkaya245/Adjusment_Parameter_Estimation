import numpy as np
from genelFonk import dolaylıModel
Px = np.array([
    [-78.26],
    [-72.10],
    [-57.84],
    [-49.11],
    [-0.66],
    [2.61],
    [15.38],
    [52.78],
    [63.88],
    [80.98]
])

Py = np.array([
    [-22.03],
    [8.00],
    [-4.90],
    [14.20],
    [42.03],
    [31.63],
    [67.97],
    [91.65],
    [80.14],
    [102.40]
])


a0 = 1
b0 = 0
W = []
A = []
x0=np.array([[1],[0]])
for i in range(len(Px)):
    # w_i = a0 * x_i + b0 - y_i
    W.append([a0 * Px[i][0] + b0 - Py[i][0]])
    A.append([Px[i][0], 1])

W = np.array(W)
A = np.array(A)
 
n=10
u=2
Cr=np.eye(10)*(50**2)
[deltaCap,rCap,xCap,lCap,CxCap,CrCap,ClCap,sig2]=dolaylıModel(A, W, Cr, x0, Py, n, u)
print(f"deltaCap\n{deltaCap}")
print(f"rCap\n{rCap}")
print(f"lCap\n{lCap}")
print(f"CxCap\n{CxCap}")
print(f"CrCap\n{CrCap}")
print(f"ClCap\n{ClCap}")
print(f"sig2Cap\n{sig2}")
print(f"xCap\n{xCap}")
CxCap
[[ 0.0020445  -0.00067973]
 [-0.00067973  0.00164858]]
deltaCap
[[ -194.10467056]
 [-9895.30375034]]
rCap
[[-1.04718976]
 [-1.04718976]
 [-1.04718976]]
sig
[[3.49914794e+10]]
ClCap
[[ 6.26784814e-11 -3.13392407e-11 -3.13392407e-11]
 [-3.13392407e-11  6.26784814e-11 -3.13392407e-11]
 [-3.13392407e-11 -3.13392407e-11  6.26784814e-11]]
CrCap
[[3.13392407e-11 3.13392407e-11 3.13392407e-11]
 [3.13392407e-11 3.13392407e-11 3.13392407e-11]
 [3.13392407e-11 3.13392407e-11 3.13392407e-11]]
lCap
[[-0.31361583]
 [ 0.10595172]
 [ 0.2076641 ]]
xCap
[[ -133.08467056]
 [-9921.57375034]]

runfile('C:/Users/Fatih BLACK/Documents/HYTO/parametre kestirimi ve dengeleme/parametreKestirmeleri/sınıfNirengi.py', wdir='C:/Users/Fatih BLACK/Documents/HYTO/parametre kestirimi ve dengeleme/parametreKestirmeleri')
Reloaded modules: fonksiyon
CxCap
[[ 0.0020445  -0.00067973]
 [-0.00067973  0.00164858]]
deltaCap
[[ -194.10467056]
 [-9895.30375034]]
rCap
[[-1.04718976]
 [-1.04718976]
 [-1.04718976]]
sig
[[3.49914794e+10]]
ClCap
[[ 6.26784814e-11 -3.13392407e-11 -3.13392407e-11]
 [-3.13392407e-11  6.26784814e-11 -3.13392407e-11]
 [-3.13392407e-11 -3.13392407e-11  6.26784814e-11]]
CrCap
[[3.13392407e-11 3.13392407e-11 3.13392407e-11]
 [3.13392407e-11 3.13392407e-11 3.13392407e-11]
 [3.13392407e-11 3.13392407e-11 3.13392407e-11]]
lCap
[[-0.31361583]
 [ 0.10595172]
 [ 0.2076641 ]]
xCap
[[ -133.08467056]
 [-9921.57375034]]

runfile('C:/Users/Fatih BLACK/Documents/HYTO/parametre kestirimi ve dengeleme/parametreKestirmeleri/sınıfNirengi.py', wdir='C:/Users/Fatih BLACK/Documents/HYTO/parametre kestirimi ve dengeleme/parametreKestirmeleri')
Reloaded modules: fonksiyon
CxCap
[[ 0.0020445  -0.00067973]
 [-0.00067973  0.00164858]]
deltaCap
[[  91.92234095]
 [1969.55852816]]
rCap
[[0.20827629]
 [0.20827629]
 [0.20827629]]
sig
[[1.38417561e+09]]
ClCap
[[ 6.26784814e-11 -3.13392407e-11 -3.13392407e-11]
 [-3.13392407e-11  6.26784814e-11 -3.13392407e-11]
 [-3.13392407e-11 -3.13392407e-11  6.26784814e-11]]
CrCap
[[3.13392407e-11 3.13392407e-11 3.13392407e-11]
 [3.13392407e-11 3.13392407e-11 3.13392407e-11]
 [3.13392407e-11 3.13392407e-11 3.13392407e-11]]
lCap
[[0.94185022]
 [1.36141777]
 [1.46313015]]
xCap
[[ 152.94234095]
 [1943.28852816]]