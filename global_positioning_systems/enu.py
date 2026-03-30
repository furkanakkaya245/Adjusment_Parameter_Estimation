import numpy as np
from paramDic_2 import D,dms_to_radian
from numpy.linalg import inv
def l(range,elev1,az1):
    elev=dms_to_radian(elev1,0,0)
    az=dms_to_radian(az1,0,0)
    return np.array([[range*np.cos(elev)*np.cos(az)],
                     [range*np.cos(elev)*np.sin(az)],
                     [range*np.sin(elev)]])
def R(phi1,lam1):
    phi=dms_to_radian(phi1,0,0)
    lam=dms_to_radian(lam1,0,0)
    return np.array([[-np.sin(phi)*np.cos(lam), -np.sin(lam), np.cos(phi)*np.cos(lam)],
                     [-np.sin(phi)*np.sin(lam), np.cos(lam),np.cos(phi)*np.sin(lam)],
                     [np.cos(phi), 0,np.sin(phi)]])
# sat_num,az,elev
rho=20200E5
sat_loc=np.array([[1,197,35],
                  [3,45,20],
                  [8,133,89],
                  [9,296,70],
                  [13,348,40]])
l_1=l(rho,sat_loc[0][1],sat_loc[0][2])
l_3=l(rho,sat_loc[1][1],sat_loc[1][2])
l_8=l(rho,sat_loc[2][1],sat_loc[2][2])
l_9=l(rho,sat_loc[3][1],sat_loc[3][2])
l_13=l(rho,sat_loc[4][1],sat_loc[4][2])

print("Uyduların Kartezyen koordinatları:")
print(l_1)
print(l_3)
print(l_8)
print(l_9)
print(l_13)

R1=R(39.887,32.758)
print(f"R1:\n{R1}")

delta_1=R1@l_1
delta_3=R1@l_3
delta_8=R1@l_8
delta_9=R1@l_9
delta_13=R1@l_13

print(f"delta_1:\n{delta_1}")

lat_1= 39.887
lon_1= 32.758
lat=dms_to_radian(lat_1,0,0)
lon=dms_to_radian(lon_1,0,0)
h=800

a=6378137.0
b=6356752.3142
e2=(a**2-b**2)/a**2
print(f"e2={e2}")


N=a/(1-(e2*(np.sin(lat))**2)*0.5)
print(f"N:{N}")
print("\nalıcı konum:")
Xr=(N+h)*np.cos(lat)*np.cos(lon)
Yr=(N+h)*np.cos(lat)*np.sin(lon)
Zr=(N*(1-e2)+h)*np.sin(lat)
print(f"Xr:{Xr}\nYr:{Yr}\nZr:{Zr}\n")

d_1=((delta_1[0][0]-Xr)**2+(delta_1[1][0]-Yr)**2+(delta_1[2][0]-Zr))**0.5
d_3=((delta_3[0][0]-Xr)**2+(delta_3[1][0]-Yr)**2+(delta_3[2][0]-Zr))**0.5
d_8=((delta_8[0][0]-Xr)**2+(delta_8[1][0]-Yr)**2+(delta_8[2][0]-Zr))**0.5
d_9=((delta_9[0][0]-Xr)**2+(delta_9[1][0]-Yr)**2+(delta_9[2][0]-Zr))**0.5
d_13=((delta_13[0][0]-Xr)**2+(delta_13[1][0]-Yr)**2+(delta_13[2][0]-Zr))**0.5


def turev(us,mesafe):
    return us/mesafe
A=np.array([[-turev(delta_1[0][0],d_1), -turev(delta_1[1][0],d_1), -turev(delta_1[2][0],d_1), 1],
            [-turev(delta_3[0][0],d_1), -turev(delta_3[1][0],d_1), -turev(delta_3[2][0],d_1), 1],
            [-turev(delta_8[0][0],d_1), -turev(delta_8[1][0],d_1), -turev(delta_8[2][0],d_1), 1],
            [-turev(delta_9[0][0],d_1), -turev(delta_9[1][0],d_1), -turev(delta_9[2][0],d_1), 1],
            [-turev(delta_13[0][0],d_1),-turev(delta_13[1][0],d_1),-turev(delta_13[2][0],d_1),1]])

print(f"A:\n{A}")

sig=3
Cxyz=(sig**2)*inv(A.T@A)

def R2enu(phi1,lam1):
    phi=dms_to_radian(phi1,0,0)
    lam=dms_to_radian(lam1,0,0)
    return np.array([[-np.sin(phi)*np.cos(lam), -np.sin(phi)*np.sin(lam), np.cos(phi)],
                     [-np.sin(lam), np.cos(lam), 0],
                     [np.cos(phi)*np.cos(lam), np.cos(phi)*np.sin(lam),np.sin(phi)]])
Cxyz_yeni=Cxyz[:3,:3]
R2=R2enu(39.887,32.758)
print(f"R2:\n{R2}")
Cneu=R2.T@Cxyz_yeni@R2

GDOP= ((Cxyz[0][0]**2+Cxyz[1][1]**2+Cxyz[2][2]**2+Cxyz[3][3]**2)/(sig**2))**0.5
HDOP= ((Cneu[1][1]**2+Cneu[0][0]**2)/(sig**2))**0.5
PDOP= ((Cneu[1][1]**2+Cneu[0][0]**2+Cneu[2][2]**2)/(sig**2))**0.5
TDOP=Cxyz[3][3]/sig
VDOP=Cneu[2][2]/sig
GDOP_1=(PDOP**2+TDOP**2)**0.5
PDOP_1=(HDOP**2+VDOP**2)**0.5

print(f"GDOP:\n{GDOP}\nHDOP:\n{HDOP}\nPDOP:\n{PDOP}\nTDOP:\n{TDOP}\nVDOP:\n{VDOP}\n")
print(f"Turetilmis GDOP:\n{GDOP_1}\nTuretilmis PDOP:\n{PDOP_1}\n")












