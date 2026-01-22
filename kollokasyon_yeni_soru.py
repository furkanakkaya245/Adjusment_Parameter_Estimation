import numpy as np
import matplotlib.pyplot as plt
# DÜZELTME 1: gauss_kernel_harici import'tan çıkarıldı
from paramDic_2 import Kollokasyon, Prediksiyon

# Hassasiyet ayarı
np.set_printoptions(precision=4, suppress=True, linewidth=200)

# =============================================================
# 1. VERİ GİRİŞİ (Slayttaki Değerler)
# =============================================================
x_val = [-96.40, -81.13, -55.72, -29.12, -11.83, 
           6.69,  37.58,  57.13,  74.11, 100.33]

y_val = [-305.39, -205.59, -109.04, -30.26, -25.30, 
            1.51,   92.71,  184.70, 214.84, 269.74]

# Soruda verilen standart sapma (+- 10)
sigma_val = 10.0

# Sınıfı Başlat
solver = Kollokasyon(x_val, y_val)

def raporla(baslik, data):
    print(f"\n{'='*60}")
    print(f"{baslik}")
    print(f"{'='*60}")
    keys = ["xCap", "sCap", "rCap", "y_total"]
    for k in keys:
        if k in data:
            val = data[k]
            # Özet geçelim (çok uzun olmasın)
            print(f"\n>>> {k} ")
            print(val[:10]) 

# =============================================================
# 2. A ŞIKKI: EKK ÇÖZÜMÜ (Sinyal İhmal)
# =============================================================
# DÜZELTME 2: 'metod' parametresi silindi. EKK için C0=0 gönderiyoruz.
sonuc_ekk = solver.coz(
    C0=0, 
    a=0,
    sigma_noise=sigma_val
)

print("\n>>> EKK Trend Parametreleri (a0, a1):")
print(sonuc_ekk["xCap"])

# =============================================================
# 3. B ŞIKKI: KOLLOKASYON ÇÖZÜMÜ
# =============================================================
# Soruda verilen parametreler: C0 = 100, a = 2
C0_soru = 100.0
a_soru = 2.0

# DÜZELTME 3: 'metod' parametresi silindi.
sonuc_kol = solver.coz(
    C0=C0_soru, 
    a=a_soru, 
    sigma_noise=sigma_val
)

raporla(f"KOLLOKASYON (C0={C0_soru}, a={a_soru})", sonuc_kol)

# =============================================================
# 4. PREDIKSIYON (KESTİRİM) - EĞRİYİ ÇİZMEK İÇİN
# =============================================================
# Modelin davranışını görmek için x aralığını sıklaştırıyoruz (-100 ile 100 arası)
predictor = Prediksiyon(solver, sonuc_kol, C0_soru, a_soru)
x_smooth = np.linspace(min(x_val)-5, max(x_val)+5, 200)
grafik_tahmin = predictor.tahmin_et(x_smooth)

# =============================================================
# 5. GRAFİKLER
# =============================================================
fig, ax = plt.subplots(1, 2, figsize=(16, 6))

# --- GRAFİK 1: Çözüm Karşılaştırması ---
# 1. Gerçek Ölçümler
ax[0].errorbar(x_val, y_val, yerr=sigma_val, fmt='ro', label='Ölçümler (+-10)', capsize=3)

# 2. EKK Doğrusu
# y = a0 + a1*x
a0_ekk, a1_ekk = sonuc_ekk["xCap"].flatten()
y_ekk_line = a0_ekk + a1_ekk * x_smooth
ax[0].plot(x_smooth, y_ekk_line, 'k--', linewidth=1.5, label='EKK (Doğru)')

# 3. Kollokasyon Eğrisi (Filtrelenmiş + Kestirilmiş)
ax[0].plot(x_smooth, grafik_tahmin["Total_p"], 'b-', linewidth=2, label='Kollokasyon (Eğri)')

# 4. Filtrelenmiş Gözlemler (Sorudaki İstek)
ax[0].scatter(x_val, sonuc_kol['y_total'], color='blue', marker='x', s=100, zorder=5, label='Filtrelenmiş Noktalar')

ax[0].set_title("EKK vs Kollokasyon Karşılaştırması")
ax[0].set_xlabel("X")
ax[0].set_ylabel("Y")
ax[0].legend()
ax[0].grid(True, linestyle=':', alpha=0.6)

# --- GRAFİK 2: Kovaryans Fonksiyonu ---
# C(tau) = C0 * exp(-a^2 * tau^2)
tau_vals = np.linspace(0, 20, 100) # Mesafeyi 0'dan 20'ye kadar alalım
# Not: Kütüphanemizdeki formül a^2 kullanır. Slayt da a^2 formülünü gösteriyor.
cov_vals = C0_soru * np.exp(-(a_soru**2) * (tau_vals**2))

ax[1].plot(tau_vals, cov_vals, 'g-', linewidth=2)

# DÜZELTME 4: LaTeX Syntax hatası düzeltildi (\\cdot ve \\tau yapıldı)
ax[1].set_title(f"Kovaryans Fonksiyonu: C($\\tau$) = {C0_soru} $\\cdot$ $e^{{-{a_soru}^2 \\tau^2}}$")
ax[1].set_xlabel("Mesafe ($\\tau$)")
ax[1].set_ylabel("Kovaryans")
ax[1].grid(True)
ax[1].text(5, 50, f"a={a_soru} olduğu için\nkorelasyon hızla\nsönümleniyor.", fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()