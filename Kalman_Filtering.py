import numpy as np
# bu soru gemili olan 
# filtrelenmis degerleri bulduk yani xCap2 sonucunu


t = [0.0,10,20.0] # zaman (sn)
x = [0.0,79.5,160.5] # konum (m)
v = [7.9,8.0,8.1] # h�z(m/s)

# t1 evresi, 1.evre çözümü

# x0 : Baslangic tahmini [konum,h�z]
x0 = np.array([0.0,7.9]).T # yaklasik degerleri aldik

# L : olculen degerler
L = np.array([x[0],v[0]]) # konum ve h�z

# Olcum matrisi 
A = np.array([[1,0],[0,1]])

# Cr : Olcum hatalar�n�n kovaryans matrisi
Cr = np.eye(2) # 1m 1m dediði için birim matris yaptik

# W : Yaklas�k degerler ile olculen degerler aras� fark
W = A@x0 - L # yaklasik deger olcum ile ayni old icin w 0 0 aldik



CxCap1 = np.linalg.inv(A.T@A) 
deltaCap1 = -np.linalg.inv(A.T@A)@A.T@W
xCap1 = x0 + deltaCap1
Ce = np.eye(2) # noise soruda birim matris olarak verilmiş.
# Ce dinamik modelin hatası
# Ce hatas� fazla olursa dinamik modelin etkisi azal�r

# t2 evresi prediction

# Gecis matrisi, yani bir epoktan diger epoka
# S : gecis matrisi -> bir epoktan diger epoka gecisi saglar
dt = t[1]-t[0]
S = np.array([[1,dt],[0,1]])
x2p = S@xCap1 # bir sonraki epok icin konum ve h�z tahmin edilir
delta2p = S@deltaCap1
Cx2p = S@CxCap1@S.T +Ce

# t2 evresi filtering
# dt = t[1]-t[0]
x02 = x2p
L2 = np.array([x[1],v[1]])
W2 = x02 - L2

# kazanc matrisi
# G : tahmin edilen degerlerin olcumle ne kadar duzeltilecegini belirler
G = Cx2p@A.T@np.linalg.inv(Cr+A@Cx2p@A.T)

deltaCap2 = delta2p-G@(A@delta2p+W2) # yaklasik degerlere gelen duzeltme
xCap2 = x02 + deltaCap2 

# kovaryans matrisini de bulalim
Cxcap2 = (np.eye(2)-G@A)@Cx2p # konum ve h�z�n varyansı, bunların karekokunu alarak da standart sapmalarını bulursun


# bundan sonra 3.epoga gececegiz ve tekrar filtrelenmis degerleri bulacagiz

# t3 evresi prediction

dt = t[2]-t[1]
S = np.array([[1,dt],[0,1]])
x3p = S@xCap2
delta3p = S@deltaCap2
Cx3p = S@Cxcap2@S.T +Ce


x03 = x3p
L = np.array([x[2],v[2]])
W3 = x03 - L
G = Cx3p@A.T@np.linalg.inv(Cr+A@Cx3p@A.T)
deltaCap3 = delta3p-G@(A@delta3p+W3)
xCap3 = x03 + deltaCap3
CxCap3 = (np.eye(2)-G@A)@Cx3p



