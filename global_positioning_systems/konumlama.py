from paramDic_2 import deltaCap_standart, Cr_
from paramDic_2 import GNSS_trilaterasyon as konumlama
import numpy as np
import math 
from numpy.linalg import inv



X1= 4124040.844
Y1= 2655252.244
Z1= 4065430.231

G06x = 5609448.760
G06y = 25140132.527
G06z = 6372861.822

G11x = 12105770.780
G11y = 23015761.543
G11z = -5496104.244

G12x = 19650283.614
G12y = -4485204.994
G12z = 16977216.177

G13x = 20485152.071
G13y = 13348417.187
G13z = -10775266.255

G15x = 26018028.018
G15y = 3827960.254
G15z = -5138658.487

G17x = -7031440.559
G17y = 13781275.560
G17z = 22038514.691

G19x = 5500349.320
G19y = 15674107.329
G19z = 20551836.203

G24x = 18243998.969
G24y = 6311666.767
G24z = 18084027.214

G25x = 19496813.820
G25y = -15213836.485
G25z = 9008928.532

G32x = 2838903.927
G32y = -15089793.387
G32z = 21815968.274



G06= 22500694.445
G11= 23877527.117
G12= 21508071.750
G13= 24417016.438
G15= 23784034.086
G17= 23699340.305
G19= 20983035.695
G24= 20205741.164
G25= 23968592.219
G32= 25215461.555


d06=konumlama(X1,Y1,Z1,G06x,G06y,G06z).d0()
d11=konumlama(X1,Y1,Z1,G11x,G11y,G11z).d0()
d12=konumlama(X1,Y1,Z1,G12x,G12y,G12z).d0()
d13=konumlama(X1,Y1,Z1,G13x,G13y,G13z).d0()
d15=konumlama(X1,Y1,Z1,G15x,G15y,G15z).d0()
d17=konumlama(X1,Y1,Z1,G17x,G17y,G17z).d0()
d19=konumlama(X1,Y1,Z1,G19x,G19y,G19z).d0()
d24=konumlama(X1,Y1,Z1,G24x,G24y,G24z).d0()
d25=konumlama(X1,Y1,Z1,G25x,G25y,G25z).d0()
d32=konumlama(X1,Y1,Z1,G32x,G32y,G32z).d0()

A=np.array([[konumlama(X1,Y1,Z1,G06x,G06y,G06z).turev()[0],konumlama(X1,Y1,Z1,G06x,G06y,G06z).turev()[1],konumlama(X1,Y1,Z1,G06x,G06y,G06z).turev()[2],1],
            [konumlama(X1,Y1,Z1,G11x,G11y,G11z).turev()[0],konumlama(X1,Y1,Z1,G11x,G11y,G11z).turev()[1],konumlama(X1,Y1,Z1,G11x,G11y,G11z).turev()[2],1],
            [konumlama(X1,Y1,Z1,G12x,G12y,G12z).turev()[0],konumlama(X1,Y1,Z1,G12x,G12y,G12z).turev()[1],konumlama(X1,Y1,Z1,G12x,G12y,G12z).turev()[2],1],
            [konumlama(X1,Y1,Z1,G13x,G13y,G13z).turev()[0],konumlama(X1,Y1,Z1,G13x,G13y,G13z).turev()[1],konumlama(X1,Y1,Z1,G13x,G13y,G13z).turev()[2],1],
            [konumlama(X1,Y1,Z1,G15x,G15y,G15z).turev()[0],konumlama(X1,Y1,Z1,G15x,G15y,G15z).turev()[1],konumlama(X1,Y1,Z1,G15x,G15y,G15z).turev()[2],1],
            [konumlama(X1,Y1,Z1,G17x,G17y,G17z).turev()[0],konumlama(X1,Y1,Z1,G17x,G17y,G17z).turev()[1],konumlama(X1,Y1,Z1,G17x,G17y,G17z).turev()[2],1],
            [konumlama(X1,Y1,Z1,G19x,G19y,G19z).turev()[0],konumlama(X1,Y1,Z1,G19x,G19y,G19z).turev()[1],konumlama(X1,Y1,Z1,G19x,G19y,G19z).turev()[2],1],
            [konumlama(X1,Y1,Z1,G24x,G24y,G24z).turev()[0],konumlama(X1,Y1,Z1,G24x,G24y,G24z).turev()[1],konumlama(X1,Y1,Z1,G24x,G24y,G24z).turev()[2],1],
            [konumlama(X1,Y1,Z1,G25x,G25y,G25z).turev()[0],konumlama(X1,Y1,Z1,G25x,G25y,G25z).turev()[1],konumlama(X1,Y1,Z1,G25x,G25y,G25z).turev()[2],1],
            [konumlama(X1,Y1,Z1,G32x,G32y,G32z).turev()[0],konumlama(X1,Y1,Z1,G32x,G32y,G32z).turev()[1],konumlama(X1,Y1,Z1,G32x,G32y,G32z).turev()[2],1]])
print(f"A={A}")
W=np.array([[d06-G06],
            [d11-G11],
            [d12-G12],
            [d13-G13],
            [d15-G15],
            [d17-G17],
            [d19-G19],
            [d24-G24],
            [d25-G25],
            [d32-G32]
            ])
print(f"W={W}")
sig=3
Cr=Cr_(10,sig)
deltaCap=deltaCap_standart(A,Cr,W)
print(f"deltaCap:\ndeltaX={deltaCap[0]}\ndeltaY={deltaCap[1]}\ndeltaZ={deltaCap[2]}")
print(f"xCap:\ndeltaX={X1+deltaCap[0]}\ndeltaY={Y1+deltaCap[1]}\ndeltaZ={Z1+deltaCap[2]}")







