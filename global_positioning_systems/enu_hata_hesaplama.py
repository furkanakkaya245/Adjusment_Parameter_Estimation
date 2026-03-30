import numpy as np
from numpy.linalg import inv

sat_loc = np.array([[1, 197, 35],
                    [3, 45, 20],
                    [8, 133, 89],
                    [9, 296, 70],
                    [13, 348, 40]])

def calculate_dops(sat_data):
    A = []
    for sat in sat_data:
        az = np.radians(sat[1])
        el = np.radians(sat[2])
        
        e = np.cos(el) * np.sin(az)
        n = np.cos(el) * np.cos(az)
        u = np.sin(el)
        
        A.append([-e, -n, -u, 1])
    
    A = np.array(A)
    Q = inv(A.T @ A) 
    

    EDOP = np.sqrt(Q[0, 0])
    NDOP = np.sqrt(Q[1, 1])
    VDOP = np.sqrt(Q[2, 2])
    TDOP = np.sqrt(Q[3, 3])
    
    HDOP = np.sqrt(EDOP**2 + NDOP**2)
    PDOP = np.sqrt(EDOP**2 + NDOP**2 + VDOP**2)
    GDOP = np.sqrt(PDOP**2 + TDOP**2)
    
    return GDOP, PDOP, HDOP, VDOP, TDOP

gdop, pdop, hdop, vdop, tdop = calculate_dops(sat_loc)
print(f"Normal Degerler:")
print(f"GDOP: {gdop:.4f}\nPDOP: {pdop:.4f}\nHDOP: {hdop:.4f}\nVDOP: {vdop:.4f}\nTDOP: {tdop:.4f}\n")
sat_loc = np.array([[1, 197, 85],
                    [3, 45, 88],
                    [8, 133, 78],
                    [9, 296, 83],
                    [13, 348, 88]])
gdop, pdop, hdop, vdop, tdop = calculate_dops(sat_loc)
print(f"Kotu Degerler:")
print(f"GDOP: {gdop:.4f}\nPDOP: {pdop:.4f}\nHDOP: {hdop:.4f}\nVDOP: {vdop:.4f}\nTDOP: {tdop:.4f}\n")
sat_loc = np.array([[1, 197, 25],
                    [3, 45, 35],
                    [8, 133, 40],
                    [9, 296, 85],
                    [13, 348, 75]])
gdop, pdop, hdop, vdop, tdop = calculate_dops(sat_loc)
print(f"Iyi Degerler:")
print(f"GDOP: {gdop:.4f}\nPDOP: {pdop:.4f}\nHDOP: {hdop:.4f}\nVDOP: {vdop:.4f}\nTDOP: {tdop:.4f}\n")