from paramDic_2 import kod_faz_kombinasyonu

m=  1.984
n=  -1.5457
sonuc=kod_faz_kombinasyonu(m,n)
print(f"Dalgaboyu: {sonuc.dalgaboyu()*100} cm")
print(f"Iyonosferik Etki: {sonuc.iyonosferik_etki()}")
print(f"Sinyal Gurultu: {sonuc.sinyal_gurultu()*1000} mm")
print(f"Oransal Gurultu: {sonuc.oransal_gurultu()}")
print(f"Frekans: {sonuc.frekans()} MHz")
