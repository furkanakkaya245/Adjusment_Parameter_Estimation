import numpy as np
from paramDic_2 import GNSS

sat_loc=np.array([[1,197,35],
                  [3,45,20],
                  [8,133,89],
                  [9,296,70],
                  [13,348,40]])

GDOP, PDOP, HDOP, VDOP, TDOP= GNSS.azimuth_elev_dop(sat_loc)
print(f"GDOP: {GDOP}")
print(f"PDOP: {PDOP}")
print(f"HDOP: {HDOP}")
print(f"VDOP: {VDOP}")
print(f"TDOP: {TDOP}")










