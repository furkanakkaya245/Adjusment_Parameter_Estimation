import scipy as sp
from scipy.stats import norm

# print(norm.ppf(0.95)) # percent point function
# print(norm.cdf(1.64485))

# Bir sınav var ortalama=60 standart sapma=10 ise öğrencilerin %70'i kaçtan daha düşük not almıştır?
#   (x-ortalama)/standart_sapma =
#   x= 52.44*standart_sapma + 60
loc=60
scale=10
print(norm.ppf(0.7,loc,scale))

# 85 alan öğrenci % kaç öğrenicden daha yüksek almıştır?
# (x-loc)/scale
print(norm.cdf(85,loc,scale))

