import math
import numpy
x1=21.94
y1=45.88
x2=-13.11
y2=-0.39
x0=61.02
y0=-26.27
x=0
y=0
l1=math.radians(42.03069)
l2=math.radians(66.07014)
l3=math.radians(71.89783)

a1x= (-1)*(1/(1+((x1-x0)/(y1-y0))**2))-(-1)*(1/(1+((x2-x0)/(y2-y0))**2))
a1xx=(-(y1-y0)**2/((y1-y)**2+(x1-x)**2))+((y2-y0)**2/((y2-y)**2+(x2-x)**2))
a1y= (((x1-x0)/(y1-y0)**2))*(1/(1+((x1-x0)/(y1-y0))**2))-(((x2-x0)/(y2-y0))**2)*(1/(1+((x2-x0)/(y2-y0)))**2)

a2x= -(1/1+((x0-x1)/(y0-y1))**2)
a2y= ((x0-x1)/(y0-y1)**2)*(1/(1+((x0-x1)/(y0-y1))**2))

a3x= 1/(1+((x0-x2)/(y0-y2))**2)
a3y=-((x0-x2)/(y0-y2)**2)*(1/(1+((x0-x2)/(y0-y2))**2))

A=numpy.array([[a1x,a1y],[a2x,a2y],[a3x,a3y]])

w31=(math.atan((x1-x0)/(y1-y0))-math.atan((x2-x0)/(y2-y0)))-l1
w32=(math.atan((x2-x1)/(y2-y1))-math.atan((x0-x1)/(y0-y1)))-l2
w33=(math.atan((x0-x2)/(y0-y2))-math.atan((x1-x2)/(y1-y2)))-l3

w=numpy.array([[w31],[w32],[w33]])

delta=numpy.array([[x-x0],[y-y0]])

r=A@delta+w

print(r)





