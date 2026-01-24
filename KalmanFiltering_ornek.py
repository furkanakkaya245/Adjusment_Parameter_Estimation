import numpy as np

t=np.array([0.0,
            9.54,
            13.11,
            19.94])

x=np.array([0.0,
            -132.75,
            -63.45,
            28.33])

v=np.array([0.0,
            6.67,
            11.67,
            16.67])

# Durum vektörü = bilinmeyenler

# t1 evresi
print("--- t1 evresi ---")
x_0=np.array([0.0,0.00])

L=np.array([x[0],v[0]])
            
A=np.array([[1,0],
            [0,1]])

Cr=np.eye(2)

W=A@x_0-L
print("W:",W)

CxCap1=np.linalg.inv(A.T@A)
deltaCap1=-CxCap1@A.T@W

print("CxCap1::",CxCap1)
print("DeltaCap1::",deltaCap1)

xCap1=x_0+deltaCap1
print("xCap1:",xCap1)

# t2 evresi prediction
print("\n--- t2 evresi ---")
# geçiş matrisi (S)

dt=t[1]-t[0]
S=np.array([[1,dt],
            [0,1]])

# noise
Ce=np.eye(2)

x2p=S@xCap1
delta2p=S@deltaCap1
Cx2p=S@CxCap1@S.T+Ce
print()
print(f"{x2p=}")
print()
print(f"{delta2p=}")
print()
print("Cx2p:",Cx2p)

# t2 evresi filtering

# dt=t[1]-t[0]

x02=x2p
L =np.array([x[1],v[1]])

W2=x02-L
print("W2",W2)

# ölçülerin mi yoksa noise un mu etkili olduğunu gösterir model üzerinde
G=Cx2p@A.T@np.linalg.inv(Cr+A@Cx2p@A.T)
print()
print("G:",G)

deltaCap2=delta2p-G@(A@delta2p+W2)
print()
print("deltaCap2:",deltaCap2)

xCap2= x02+deltaCap2
print()
print("xcap2:",xCap2)

CxCap2=(np.eye(2)-G@A)@Cx2p
print()
print("CxCap2:",CxCap2)

# t3 evresi prediction
print("\n--- t3 evresi ---")
dt=t[2]-t[1]
S=np.array([[1,dt],
            [0,1]])
# noise
# Ce burada dinamik modeli temsil eder
# Yani Ce ne kadar büyürse Dinamik modelin etkisi azalır
Ce=np.eye(2)

x3p=S@xCap2
delta3p=S@deltaCap2
Cx3p=S@CxCap2@S.T+Ce
print()
print(f"{x3p=}")
print()
print(f"{delta3p=}")
print()
print("Cx3p:",Cx3p)
print()

# t3 evresi filtering

# dt=t[2]-t[1]

x03=x3p
L =np.array([x[2],v[2]])

W3=x03-L
print("W3",W3)

# ölçülerin mi yoksa noise un mu etkili olduğunu gösterir model üzerinde
G=Cx3p@A.T@np.linalg.inv(Cr+A@Cx3p@A.T)
print()
print("G:",G)

deltaCap3=delta3p-G@(A@delta3p+W3)
print()
print("deltaCap3:",deltaCap3)

xCap3= x03+deltaCap3
print()
print("xcap3:",xCap3)

CxCap3=(np.eye(2)-G@A)@Cx3p
print("CxCap3:",CxCap3)