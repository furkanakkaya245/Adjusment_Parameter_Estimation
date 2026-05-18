import numpy as np
from paramDic_2 import dms_to_radian,troposferic_delay,mapping_func
import math
# Saastamoinen Model
# p milibar olarak verilemlidir

phi= 41.5 # derece
h= 2500   # m
e= 30     # mbar
p= 1      # atm
t= 25     # santigrad
print(f"Nokta Enlemi           = {phi} derece")
print(f"Nokta Yuksekligi       = {h} m")
print(f"Kismi Su Buhar Basinci = {e} mbar")
print(f"Basinc                 = {p} atm")
print(f"Sicaklik               = {t} santigrad" )
# zenit = 0
deger1=troposferic_delay(phi,h)
dry_delay=deger1.d_kuru(p)
wet_Delay=deger1.d_islak(t,e)
print(f"Dry Delay : {dry_delay} m")
print(f"Wet Delay : {wet_Delay} m")
# zenit = 70
deger2=troposferic_delay(phi,h)
dry_delay=deger1.d_kuru(p)*mapping_func(70)
wet_Delay=deger1.d_islak(t,e)*mapping_func(70)
print(f"Dry Delay : {dry_delay} m")
print(f"Wet Delay : {wet_Delay} m")

