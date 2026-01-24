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
        self.ilkOlcum = ilkOlcum  
        self.ikinciOlcum = ikinciOlcum 
        self.sig = sig
        
       
        self.A1 = A[:self.ilkOlcum, :]  # A1 matrisi: 6x2
        self.W1 = W[:self.ilkOlcum, :]  # W1 matrisi: 6x1
        
       
        self.A2 = A[self.ilkOlcum:, :]  # A2 matrisi: 6x2
        self.W2 = W[self.ilkOlcum:, :]  # W2 matrisi: 6x1

    

    def __Cr1(self):
        
        return np.eye(self.ilkOlcum) * (self.sig**2)
    
    def __Cr2(self):
        
        return np.eye(self.ikinciOlcum) * (self.sig**2)
    
    def __N1(self):
       
        return self.A1.T @ inv(self.__Cr1()) @ self.A1
    
    def __N2(self):
        
        return self.A2.T @ inv(self.__Cr2()) @ self.A2
    
    def __M(self):
        
        return inv(self.__Cr2())
    


    def deltaCap(self):
       
        return -(inv(self.__N1()) @ self.A1.T @ inv(self.__Cr1()) @ self.W1)
    
    def deltaS(self):
        
        C_delta_x1 = inv(self.__N1()) 
        
        V = inv(self.__M()) + (self.A2 @ C_delta_x1 @ self.A2.T)
        
        return (-C_delta_x1 @ self.A2.T) @ inv(V) @ ((self.A2 @ self.deltaCap()) + self.W2)
    
    def direktDeltaCapSon(self):
        
        u1 = self.A1.T @ inv(self.__Cr1()) @ self.W1
        u2 = self.A2.T @ inv(self.__Cr2()) @ self.W2
        return -(inv(self.__N1() + self.__N2())) @ (u1 + u2)
    
    def birliteDeltaCapSon(self):
        
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
        
        self.S_kare = self.Payda
        
    def gradyan_hesapla(self):
        dx1 = -self.Dy / self.S_kare 
        dy1 = self.Dx / self.S_kare 
        dx2 = self.Dy / self.S_kare 
        dy2 = -self.Dx / self.S_kare 
        return dx1, dy1, dx2, dy2
def Kalman_Sabit_Hiz(x_prev, Cx_prev, delta_prev, L_curr, S, A, Cr, Ce):
    I = np.eye(len(x_prev))
    x_pred = S @ x_prev
    Cx_pred = (S @ Cx_prev @ S.T) + Ce
    delta_pred = S @ delta_prev
    K = Cx_pred
    G = K @ A.T @ inv((A @ K @ A.T) + Cr)
    W = (A @ x_pred) - L_curr
    delta_curr = delta_pred - (G @ (W + (A @ delta_pred)))
    x_curr = x_pred + delta_curr
    Cx_curr = (I - G @ A) @ Cx_pred
    return x_curr, Cx_curr, delta_curr, G

class Kollokasyon:
    def __init__(self, x_coords):
        self.x = np.array(x_coords)
        self.n = len(self.x)
        self.A = np.column_stack((np.ones(self.n), self.x))
    def _gauss_kernel(self, C0, a):
        Cs = np.zeros((self.n, self.n))
        if C0 == 0:
            return Cs   
        for i in range(self.n):
            for j in range(self.n):
                tau = self.x[j] - self.x[i]
                Cs[i, j] = C0 * np.exp(-(a**2) * (tau**2))
        return Cs
    def hesapla(self, W, x0, C0, a, sigma_noise):
        W = np.array(W).reshape(-1, 1)
        x0 = np.array(x0).reshape(-1, 1)
        Cr = np.eye(self.n) * (sigma_noise**2)  # Gürültü (Mv)
        Cs = self._gauss_kernel(C0, a)          # Sinyal (Ms)
        # M = inv(Cs + Cr)
        M = np.linalg.inv(Cs + Cr)
        # N = inv(A' * M * A)
        N = np.linalg.inv(self.A.T @ M @ self.A)
        # L = M - M*A*N*A'*M
        L_mat = M - (M @ self.A @ N @ self.A.T @ M)
        deltaCap = -N @ self.A.T @ M @ W
        xCap = x0 + deltaCap
        sCap = Cs @ L_mat @ W
        rCap = Cr @ L_mat @ W
        y_trend = self.A @ xCap
        y_total = y_trend + sCap
        return xCap, deltaCap, sCap, rCap, M, N, L_mat, Cs, Cr, y_total

class Prediksiyon:
    def __init__(self, solver_obj, result_dict, C0, a):
        self.x_train = solver_obj
        self.res = result_dict
        self.C0 = C0
        self.a = a
        self.T = np.eye(len(self.x_train))
    def _gauss_kernel(self, x1, x2, C0, a):
        n1 = len(x1)
        n2 = len(x2)
        C = np.zeros((n1, n2))
        if C0 == 0:
            return C   
        for i in range(n1):
            for j in range(n2):
                tau = x2[j] - x1[i]
                C[i, j] = C0 * np.exp(-(a**2) * (tau**2))
        return C
    def hesapla(self, x_p_coords):
        x_p = np.array(x_p_coords)
        L = self.res["L"]
        w = self.res["w"]
        xCap = self.res["xCap"]
        sCap_train = self.res["sCap"]
        Csps = self._gauss_kernel(x_p, self.x_train, self.C0, self.a)
        SpCap = -Csps @ self.T.T @ L @ w
        A_p = np.column_stack((np.ones(len(x_p)), x_p))
        Trend_p = A_p @ xCap
        Total_p = Trend_p + SpCap
        z_vector = np.vstack((SpCap, sCap_train))
        return x_p, Csps, SpCap, Trend_p, Total_p, z_vector


class KalmanFiltresi:
    def __init__(self, model_tipi="sabit_hiz"):
        self.model_tipi = model_tipi
    def adim_hesapla(self, x_prev, Cx_prev, delta_prev, L_curr, dt, A, Cr, Ce):
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
        return x_curr, Cx_curr, delta_curr, G,W,S,Cx_pred,x_pred,x_prev


