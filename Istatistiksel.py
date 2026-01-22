import scipy as sp
from scipy.stats import norm
from scipy.stats import chi2
from scipy.stats import t
from scipy.stats import f

import numpy as np

# print(norm.ppf(0.95)) # percent point function
# print(norm.cdf(1.64485))

# NORMAL DAĞILIM
# Bir sınav var ortalama=60 standart sapma=10 ise öğrencilerin %70'i kaçtan daha düşük not almıştır?
#   (x-ortalama)/standart_sapma =
#   x= 52.44*standart_sapma + 60
loc=60
scale=10
# print(norm.ppf(0.7,loc,scale))

# print(norm.cdf(2.4,loc=1,scale=2))

# 85 alan öğrenci % kaç öğrenicden daha yüksek almıştır?
# (x-loc)/scale
# print(norm.cdf(85,loc,scale))

# Kİ-KARE DAĞILIMI
# varyans = (r.T@inv(Cr)@r)/(n-u) (n-u) serbestlik derecesi
# print(chi2.pdf(0.9,df=5))

# T-DAĞILIMI
# t.pdf(0.025)
# t.pdf(0.975) olasılıklara denk gelen nokta değerleri

# Direkt ve Ters Problemler
# olasılık verilip değer bulunması       : Ters      ppf
# değer verilip olasılığının bulunması   : Direkt    cdf

loc=1
scale= 4**0.5
print(f"1-a: {norm.cdf(2.4,loc,scale)}")
print(f"1-b: {norm.cdf(-1.1,loc,scale)}")
print(f"1-c: {1-norm.cdf(1.1,loc,scale)}")
print(f"1-d: {norm.cdf(8,loc,scale)-norm.cdf(2,loc,scale)}\n")

loc=0
scale= 1**0.5
print(f"2-a: {norm.ppf(0.10,loc,scale)}")
print(f"2-b: {norm.ppf(0.20,loc,scale)}")
print(f"2-c: {norm.ppf((1-0.05),loc,scale)}")
print(f"2-d: {norm.ppf(0.975,loc,scale)}\n") # 0.95 in ortada olması için

loc=1
scale=0.01**0.5
print(f"3-a: {1-(norm.cdf(1.02,loc,scale)-norm.cdf(0.98,loc,scale))}")
ust_sinir = norm.ppf(0.995, loc, scale)
alt_sinir = norm.ppf(0.005, loc, scale)
print(f"3-b: [{alt_sinir:.4f} mm, {ust_sinir:.4f} mm]")


