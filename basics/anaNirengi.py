import numpy as np
import math
from genelFonk import dolaylıModel, dms_to_radian
import sympy as sp

def tanIc(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)
def tan(x1,y1,x2,y2):
    return math.atan2((y2-y1),(x2-x1))

def dy(x1,y1,x2,y2):
    return 1/(x2-x1)
def dx(x1,y1,x2,y2):
    return (y2-y1)/((x2-x1)**2)
def dTan(x1,y1,x2,y2):
    return 1/(1+(tanIc(x1, y1, x2, y2))**2)

C1x= 21.94
C1y= 45.88

C2x= -13.11
C2y= -0.39

L1=dms_to_radian(42.03069, 0, 0)
L2=dms_to_radian(66.07014, 0, 0)
L3=dms_to_radian(71.89783, 0, 0)
sig= dms_to_radian(0, 0, 2)

Px0= 61.02
Py0= -26.27




x, y, x0, y0 = sp.symbols('x y x0 y0')
f = sp.atan((y - y0) / (x - x0))

df_dx0 = sp.diff(f, x0)
df_dy0 = sp.diff(f, y0)
df_dx00 = sp.diff(f, x)
df_dy00 = sp.diff(f, y)

f_dx0 = sp.lambdify((x, y, x0, y0), df_dx0, 'numpy')
f_dy0 = sp.lambdify((x, y, x0, y0), df_dy0, 'numpy')
f_dx00 = sp.lambdify((x, y, x0, y0), df_dx00, 'numpy')
f_dy00 = sp.lambdify((x, y, x0, y0), df_dy00, 'numpy')

AL1x = f_dx0(C1x, C1y, Px0, Py0) - f_dx0(C2x, C2y, Px0, Py0)
AL1y = f_dy0(C1x, C1y, Px0, Py0) - f_dy0(C2x, C2y, Px0, Py0)

AL2x = -f_dx00(Px0, Py0, C1x, C1y)  
AL2y = -f_dy00(Px0, Py0, C1x, C1y)

AL3x = f_dx00(Px0, Py0, C2x, C2y)
AL3y = f_dy00(Px0, Py0, C2x, C2y)

A=np.array([[AL1x,AL1y],
           [AL2x,AL2y],
           [AL3x,AL3y]])


W = np.array([
    [ (tanIc(Px0, Py0, C1x, C1y) - tanIc(Px0, Py0, C2x, C2y)) - L1 ],
    [ (tanIc(C1x, C1y, C2x, C2y) - tanIc(C1x, C1y, Px0, Py0)) - L2 ],
    [ (tanIc(C2x, C2y, Px0, Py0) - tanIc(C2x, C2y, C1x, C1y)) - L3 ]
])
Cr=np.eye(3)*(sig**2)
yak=np.array([[Px0],
              [Py0]])
olc=np.array([[L1],
              [L2],
              [L3]])
deltaCap, rCap, xCap, lCap, CxCap, CrCap, ClCap, sig2 = dolaylıModel(A, W, Cr, yak, olc, n=3, u=2)

print(f"deltaCap\n{deltaCap}")
print(f"rCap\n{rCap}")
print(f"lCap\n{lCap}")
print(f"CxCap\n{CxCap}")
print(f"CrCap\n{CrCap}")
print(f"ClCap\n{ClCap}")
print(f"sig2Cap\n{sig2}")
print(f"xCap\n{xCap}")
print(f"A\n{A}")

             
             
