from paramDic_2 import deltaCap_standart,rCap_,Cr_
import numpy as np

H1=66.08
H2=199.32

A=np.array([[-1,1],
            [-1,0],
            [-1,0],
            [0,-1],
            [0,-1]])
l1=-190.33
l2=-168.41
l3=-299.78
l4=-166.54
l5=21.93

sig=0.02

W=np.array([[-l1],
            [H1-l2],
            [H2-l3],
            [H1-l4],
            [H2-l5]])

Cr=Cr_(5,sig)

deltaCap=deltaCap_standart(A,Cr,W)
rCap=rCap_(A,deltaCap,W)

print(f"deltaCap:\n{deltaCap}")
print(f"rCap:\n{rCap}")
      
