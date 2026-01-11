import numpy as np
from numpy.linalg import inv
import math

def mesafe(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    return math.hypot(dx,dy)
def N_standart(A,Cr):
    return A.T@inv(Cr)@A
def dms_to_radian(derece, dakika, saniye):
    decimal_degree = derece + dakika / 60 + saniye / 3600
    radian = math.radians(decimal_degree)
    return radian
def deltaCap_standart(A_,Cr_,W_):    
    return -(inv(N_standart(A_,Cr_))@A_.T@inv(Cr_)@W_)
def deltaCap_Bayesian(A_,Cr_,W_,C0_):
    return -((inv(inv(C0_)+N_standart(A_,Cr_)))@(A_.T@inv(Cr_)@W_))
def xCap(x0,deltaCap):
    return x0+deltaCap
def Cr_(olcu_say,hata):
    return np.eye(olcu_say)*(hata**2)
def C0(param,hata):
    return np.eye(param)*(hata**2)
def rCap_(A,deltaCap,W):
    return A@deltaCap+W
def CxCap_(A,Cr):
    return inv(A.T@inv(Cr)@A)
def CrCap_(A,Cr,N):
    return Cr-(A@inv(N_standart(A,Cr))@A.T)
def ClCap_(A,Cr):
    return A@inv(N_standart(A,Cr))@A.T
def kosullu_deltaCap(A,Ac,W,Wc,Cr,olcum_say,sig_olcum):
    def deltaCap_(A,W):
        return (-(inv(N_standart(A,Cr_(olcum_say,sig_olcum)))@A.T@inv(Cr_(olcum_say,sig_olcum))@W))
    def DdeltaCap(Ac,Wc):
        return -(N_standart(A,Cr_(olcum_say,sig_olcum))@Ac.T)@inv(Ac@N_standart(A,Cr_(olcum_say,sig_olcum))@Ac.T)@(Wc+(Ac@deltaCap_(A,W)))
    def DdeltaCap_(A,Cr,W,Ac,Wc):
        return inv(N_standart(A,Cr))@Ac.T@inv(Ac@inv(N_standart(A,Cr))@Ac.T)@(Wc+Ac@deltaCap_standart(A,Cr,W))
    return deltaCap_standart(A,Cr,W)-DdeltaCap_(A,Cr,W,Ac,Wc)
def L(d1,d2):
        return d1-d2

class Direkt_AdimAdim_Cozum:
    def __init__(self,ilkOlcum,ikinciOlcum,A,W,sig):
        self.ilkOlcum=ilkOlcum
        self.ikinciOlcum=ikinciOlcum
        self.A2=A
        self.W2=W
        self.sig=sig
        self.A1=self.A2[:self.ilkOlcum:]
        self.W1=self.W2[:self.ilkOlcum:]
        

    def __Cr1(self):
        return np.eye(self.ilkOlcum)*(self.sig**2)
    
    def __Cr2(self):
        return np.eye(self.ikinciOlcum)*(self.sig**2)
    
    def __N1(self):
        return self.A1.T@inv(self.__Cr1())@self.A1
    
    def __N2(self):
        return self.A2.T@inv(self.__Cr2())@self.A2
    
    def __u1(self):
        return self.A1.T@inv(self.__Cr1())@self.W1
    
    def __u2(self):
        return self.A2.T@inv(self.__Cr2())@self.W2
    
    def __M(self):
        return inv(self.__Cr2())
    
    def deltaCap(self):
        return -(inv(self.__N1())@self.A1.T@inv(self.__Cr1())@self.W1)
    
    def deltaS(self):
        return (-inv(self.__N1())@self.A2.T)@inv(inv(self.__M())+(self.A2@inv(self.__N1())@self.A2.T))@((self.A2@self.deltaCap())+self.W2)
    
    def CdeltaCapSon(self):
        return (self.__Cr1())-((self.__Cr1()@self.A2.T)@inv(inv(self.__M())+(self.A2@self.__Cr1()@self.A2.T)))@(self.A2@self.__Cr1())
    
    def direktDeltaCapSon(self):
        return -(inv(self.__N1()+self.__N2()))@((self.A1.T@inv(self.__Cr1())@self.W1)+(self.A2.T@inv(self.__Cr2())@self.W2))
    
    def birliteDeltaCapSon(self):
        return self.deltaCap()+self.deltaS()

class Direkt_AdimAdim_Cozum_Trilaterasyon:
    
    def __init__(self, ilkOlcum, ikinciOlcum, A, W, sig):
        self.ilkOlcum = ilkOlcum  # n1 = 6
        self.ikinciOlcum = ikinciOlcum  # n2 = 6
        self.sig = sig
        
        # 1. Aşama Gözlemleri (İlk 6)
        self.A1 = A[:self.ilkOlcum, :]  # A1 matrisi: 6x2
        self.W1 = W[:self.ilkOlcum, :]  # W1 matrisi: 6x1
        
        # 2. Aşama Gözlemleri (Sonraki 6)
        # HATA DÜZELTİLDİ: A2 ve W2, A ve W'nun kalan kısmıdır.
        self.A2 = A[self.ilkOlcum:, :]  # A2 matrisi: 6x2
        self.W2 = W[self.ilkOlcum:, :]  # W2 matrisi: 6x1

    # --- Kovaryans ve Normal Matris Fonksiyonları ---

    def __Cr1(self):
        """1. aşama gözlemleri için kovaryans matrisi (6x6)"""
        return np.eye(self.ilkOlcum) * (self.sig**2)
    
    def __Cr2(self):
        """2. aşama gözlemleri için kovaryans matrisi (6x6)"""
        return np.eye(self.ikinciOlcum) * (self.sig**2)
    
    def __N1(self):
        """1. aşama normal matrisi (2x2)"""
        return self.A1.T @ inv(self.__Cr1()) @ self.A1
    
    def __N2(self):
        """2. aşama normal matrisi (2x2)"""
        return self.A2.T @ inv(self.__Cr2()) @ self.A2
    
    def __M(self):
        """Gözlem Kovaryans Matrisinin Tersidir: C_r2^-1 (6x6)"""
        return inv(self.__Cr2())
    
    # --- Kestirim Fonksiyonları ---

    def deltaCap(self):
        """İlk aşama düzeltmesi (delta_x1)"""
        return -(inv(self.__N1()) @ self.A1.T @ inv(self.__Cr1()) @ self.W1)
    
    def deltaS(self):
        """İkinci aşamadan gelen düzeltme vektörü (delta_s)"""
        # C_delta_x1 = N1^-1 (İlk kestirimin kovaryans matrisi)
        C_delta_x1 = inv(self.__N1()) 
        
        # V = (M^-1 + A2 * C_delta_x1 * A2.T)
        V = inv(self.__M()) + (self.A2 @ C_delta_x1 @ self.A2.T)
        
        # delta_s = - C_delta_x1 * A2.T * inv(V) * (A2 * delta_x1 + W2)
        return (-C_delta_x1 @ self.A2.T) @ inv(V) @ ((self.A2 @ self.deltaCap()) + self.W2)
    
    def direktDeltaCapSon(self):
        """Tüm gözlemleri tek adımda kullanarak elde edilen sonuç (Direkt Kestirim)"""
        # N_toplam = N1 + N2
        # u_toplam = u1 + u2
        u1 = self.A1.T @ inv(self.__Cr1()) @ self.W1
        u2 = self.A2.T @ inv(self.__Cr2()) @ self.W2
        return -(inv(self.__N1() + self.__N2())) @ (u1 + u2)
    
    def birliteDeltaCapSon(self):
        """Adım Adım Kestirim Sonucu: delta_x1 + delta_s"""
        return self.deltaCap() + self.deltaS()

class trilaterasyon_cozum:
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def d0(self):
        d0=mesafe(self.x1,self.y1,self.x2,self.y2)
        return d0
    def turev(self):
        dx1=(-1)*(self.x2-self.x1)/(self.d0())
        dy1=(-1)*(self.y2-self.y1)/(self.d0())
        dx2=(self.x2-self.x1)/(self.d0())
        dy2=(self.y2-self.y1)/(self.d0())
        return dx1,dy1,dx2,dy2
    
class triangulasyon_aci:
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def aTan(self):
        return math.atan2()

    def __FarkEl(self):
        Dx=self.x2-self.x1
        Dy=self.y2-self.y1
        return Dx,Dy
    def __ortak(self):
        kareX=(self.__FarkEl()[0])**2
        kareY=(self.__FarkEl()[1])**2
        cikti=(kareX**2)/(kareY**2+kareX**2)
        return 1/(1+cikti)
    def __Fx(self):
        return self.__FarkEl()[1]/(self.__FarkEl()[0])**2
    def __Fy(self):
        return 1/(self.__FarkEl()[0])
    def turevX(self):
        return self.__ortak()*self.__Fx()
    def turevY(self):
        return self.__ortak()*self.__Fy()
    def turev(self):
        dx1=(-1)*self.__ortak()*self.__Fx()
        dy1=(-1)*self.__ortak()*self.__Fy()
        dx2=self.__ortak()*self.__Fx()
        dy2=self.__ortak()*self.__Fy()
        return dx1,dy1,dx2,dy2
    def aTan0(self):
        return math.atan2(self.__FarkEl()[1],self.__FarkEl()[0])

class trilaterasyon_cozum:
    # ... (Trilaterasyon class'ı aynı kalacak) ...
    def __init__(self,x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def d0(self):
        d0=mesafe(self.x1,self.y1,self.x2,self.y2)
        return d0
    def turev(self):
        dx1=(-1)*(self.x2-self.x1)/(self.d0())
        dy1=(-1)*(self.y2-self.y1)/(self.d0())
        dx2=(self.x2-self.x1)/(self.d0())
        dy2=(self.y2-self.y1)/(self.d0())
        return dx1,dy1,dx2,dy2

class TriangulasyonAciGradyan:
    def __init__(self, x1, y1, x2, y2):
        self.Dx = x2 - x1
        self.Dy = y2 - y1
        self.Payda = self.Dx**2 + self.Dy**2
        
        if self.Payda == 0:
            raise ValueError("Noktalar çakışıyor! Türev paydası sıfır olamaz.")
        
        # Ortak terimler: S^2
        self.S_kare = self.Payda
        
    def gradyan_hesapla(self):
        
        # d(açı)/d(parametre) formülleri:
        # d(açı)/dx = Dy / S^2
        # d(açı)/dy = -Dx / S^2
        
        # d(açı) / dx1 = (Dy / S^2) * (-1) = -Dy / S^2
        dx1 = -self.Dy / self.S_kare 
        
        # d(açı) / dy1 = (-Dx / S^2) * (-1) = Dx / S^2
        dy1 = self.Dx / self.S_kare 
        
        # d(açı) / dx2 = (Dy / S^2) * (1) = Dy / S^2
        dx2 = self.Dy / self.S_kare 
        
        # d(açı) / dy2 = (-Dx / S^2) * (1) = -Dx / S^2
        dy2 = -self.Dx / self.S_kare 
        
        return dx1, dy1, dx2, dy2

class kollakasyon:
    def __init__(self,olcu_say,olcu_hata,A,W,C0,T,xs,a):
        self.olcu_say=olcu_say
        self.olcu_hata=olcu_hata
        self.T=T
        self.A=A
        self.W=W
        self.C0=C0
        self.xs=xs
        self.a=a
    def __Cs(self):
        n = len(self.xs)
        Cs = np.zeros([n,n])
        for i in range(n):
            for j in range(n):
                Tau = self.xs[j]-self.xs[i]
                Cs[i,j] = self.C0 * math.exp(-1*self.a*Tau**2)
        return Cs
    def __M(self):
        return inv(self.T@self.__Cs()@self.T.T+Cr_(self.olcu_say,self.olcu_hata))
    def __N(self):
        return inv(self.A.T@self.__M()@self.A)
    def __deltaCap(self):
        return -(self.__N()@self.A.T@self.__M()@self.W)
    def __L(self):
        return self.__M()-(self.__M()@self.A@self.__N()@self.A.T@self.__M())
    def __sCap(self):
        return self.__Cs()@self.T.T@self.__L()@self.W
    def __rCap(self):
        return Cr_(self.olcu_say,self.olcu_hata)@self.__L()@self.W
    def __CrCap(self):
        return Cr_(self.olcu_say,self.olcu_hata)@self.__L()@Cr_(self.olcu_say,self.olcu_hata)
    def __CsCap(self):
        return self.__Cs()@self.T.T@self.__L()@self.T@self.__Cs()
    def __CsCaprCap(self):
        return self.__Cs()@self.T.T@self.__L()@Cr_(self.olcu_say,self.olcu_hata)
    def sonuc(self):
        deltaCap=self.__deltaCap()
        sCap=self.__sCap()
        rCap=self.__rCap()
        CrCap=self.__CrCap()
        CsCap=self.__CsCap()
        CsrCap=self.__CsCaprCap()
        Cs=self.__Cs()
        L=self.__L()
        return deltaCap,sCap,rCap,CrCap,CsCap,CsrCap,Cs,L

def Kalman_Sabit_Hiz(x_prev, Cx_prev, delta_prev, L_curr, S, A, Cr, Ce):
    """
    - x_prev: Bir önceki evrenin durum vektörü (x_cap)
    - Cx_prev: Bir önceki evrenin kovaryans matrisi (Cx_cap)
    - delta_prev: Bir önceki evrenin düzeltme miktarı (delta_cap)
    - L_curr: Mevcut evrenin ölçüm vektörü
    - S: Geçiş matrisi
    - A: Ölçüm katsayılar matrisi (H)
    - Cr: Ölçüm gürültüsü (R)
    - Ce: Sistem gürültüsü (Q)
    """
    I = np.eye(len(x_prev))
    
    # --- 1. Tahmin (Prediction) ---
    x_pred = S @ x_prev
    Cx_pred = (S @ Cx_prev @ S.T) + Ce
    delta_pred = S @ delta_prev
    
    # --- 2. Kazanç (Gain) ---
    K = Cx_pred
    G = K @ A.T @ inv((A @ K @ A.T) + Cr)
    
    # --- 3. Güncelleme (Update) ---
    W = (A @ x_pred) - L_curr
    delta_curr = delta_pred - (G @ (W + (A @ delta_pred)))
    
    x_curr = x_pred + delta_curr
    Cx_curr = (I - G @ A) @ Cx_pred
    
    return x_curr, Cx_curr, delta_curr, G


class KalmanFiltresi:
    def __init__(self, model_tipi="sabit_hiz"):
        """
        model_tipi: "sabit_hiz" veya "sabit_ivme"
        """
        self.model_tipi = model_tipi
        
    def adim_hesapla(self, x_prev, Cx_prev, delta_prev, L_curr, dt, A, Cr, Ce):
        """
        - x_prev: Durum vektörü 
        - Cx_prev: Kovaryans matrisi 
        - delta_prev: Düzeltme vektörü 
        - L_curr: Ölçüm vektörü 
        - dt: Zaman farkı
        - A: Ölçüm matrisi 
        - Cr: Ölçüm gürültüsü 
        - Ce: Sistem gürültüsü 
        """
        n = len(x_prev)
        I = np.eye(n)
       
        if self.model_tipi == "sabit_hiz":
            if n == 2: 
                S = np.array([[1, dt],
                              [0, 1]])
            elif n == 4: 
                S = np.array([[1, 0, dt, 0],
                              [0, 1, 0, dt],
                              [0, 0, 1, 0],
                              [0, 0, 0, 1]])
        
        elif self.model_tipi == "sabit_ivme":
            if n == 3: 
                S = np.array([[1, dt, 0.5 * dt**2],
                              [0, 1, dt],
                              [0, 0, 1]])
            elif n == 6: 
                S = np.array([[1, 0, dt, 0, 0.5 * dt**2, 0],
                              [0, 1, 0, dt, 0, 0.5 * dt**2],
                              [0, 0, 1, 0, dt, 0],
                              [0, 0, 0, 1, 0, dt],
                              [0, 0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 0, 1]])
        

        x_pred = S @ x_prev
        Cx_pred = (S @ Cx_prev @ S.T) + Ce
        delta_pred = S @ delta_prev
        K = Cx_pred
        G = K @ A.T @ inv(A @ K @ A.T + Cr)
        W = (A @ x_pred) - L_curr 
        delta_curr = delta_pred - (G @ (W + (A @ delta_pred)))
        x_curr = x_pred + delta_curr
        Cx_curr = (I - G @ A) @ Cx_pred
        return x_curr, Cx_curr, delta_curr, G


        
    


    
        
