import sys
import numpy as np
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QTextEdit, QPushButton, 
                             QTabWidget, QFormLayout, QMessageBox, QGroupBox, QComboBox)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# SENİN KÜTÜPHANENİ IMPORT EDİYORUZ
try:
    import paramDic_2 as pd2
except ImportError:
    print("HATA: 'paramDic_2.py' dosyası bulunamadı.")
    sys.exit(1)

# --- YARDIMCI WIDGET'LAR ---
class MatrixInput(QTextEdit):
    """Matris verilerini string olarak alıp numpy array'e çeviren widget."""
    def __init__(self, default_text=""):
        super().__init__()
        self.setPlainText(default_text)
        self.setMaximumHeight(80)
    
    def get_matrix(self):
        try:
            text = self.toPlainText().strip()
            rows = text.split(';')
            matrix = []
            for row in rows:
                if row.strip():
                    matrix.append([float(x) for x in row.split(',')])
            return np.array(matrix)
        except Exception as e:
            raise ValueError(f"Matris format hatası! Örnek: '1,2; 3,4' \nHata: {str(e)}")

class MplCanvas(FigureCanvas):
    """Matplotlib grafikleri için PyQt widget'ı."""
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

# --- MODÜL 1: KOLLOKASYON SEKME ---
class KollokasyonTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        
        # Sol Panel
        input_group = QGroupBox("Veri Girişi")
        form = QFormLayout()
        
        self.in_x = MatrixInput("1, 2, 3, 4, 5, 6")
        self.in_l = MatrixInput("10.1, 12.2, 13.8, 16.1, 18.2, 20.3")
        self.in_C0 = QTextEdit("10.0"); self.in_C0.setMaximumHeight(30)
        self.in_a = QTextEdit("0.5"); self.in_a.setMaximumHeight(30)
        
        form.addRow("X Koordinatları:", self.in_x)
        form.addRow("Ölçümler (L):", self.in_l)
        form.addRow("Sinyal Varyansı (C0):", self.in_C0)
        form.addRow("Korelasyon (a):", self.in_a)
        
        self.btn_calc = QPushButton("Hesapla ve Çiz")
        self.btn_calc.clicked.connect(self.hesapla)
        
        input_group.setLayout(form)
        input_group.layout().addWidget(self.btn_calc)
        
        # Sağ Panel
        self.canvas = MplCanvas(self)
        layout.addWidget(input_group, 30)
        layout.addWidget(self.canvas, 70)
        self.setLayout(layout)

    def hesapla(self):
        try:
            x_raw = self.in_x.get_matrix().flatten()
            l_raw = self.in_l.get_matrix().flatten()
            C0 = float(self.in_C0.toPlainText())
            a = float(self.in_a.toPlainText())
            
            solver = pd2.Kollokasyon(x_raw, l_raw)
            sonuc = solver.coz(C0=C0, a=a, sigma_noise=0.1)
            
            self.canvas.axes.cla()
            self.canvas.axes.scatter(x_raw, l_raw, c='red', label='Ölçümler', zorder=5)
            self.canvas.axes.plot(x_raw, sonuc['y_trend'], 'g--', label='Trend')
            self.canvas.axes.plot(x_raw, sonuc['y_total'], 'b-', label='Kestirim')
            self.canvas.axes.legend()
            self.canvas.axes.grid(True)
            self.canvas.axes.set_title("Kollokasyon Analizi")
            self.canvas.draw()
        except Exception as e:
            QMessageBox.critical(self, "Hata", str(e))

# --- MODÜL 2: ADIM ADIM ÇÖZÜM SEKME ---
class AdimAdimTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        form = QFormLayout()
        
        self.in_ilk = QTextEdit("6"); self.in_ilk.setMaximumHeight(30)
        self.in_ikinci = QTextEdit("6"); self.in_ikinci.setMaximumHeight(30)
        self.in_sig = QTextEdit("0.01"); self.in_sig.setMaximumHeight(30)
        self.in_A = MatrixInput("1,0; 1,0; 1,0; 1,0; 1,0; 1,0; 0,1; 0,1; 0,1; 0,1; 0,1; 0,1") 
        self.in_W = MatrixInput("0.1; 0.2; 0.1; 0.0; -0.1; 0.2; 0.5; 0.4; 0.6; 0.5; 0.5; 0.4")
        
        form.addRow("n1:", self.in_ilk)
        form.addRow("n2:", self.in_ikinci)
        form.addRow("Sigma0:", self.in_sig)
        form.addRow("A Matrisi:", self.in_A)
        form.addRow("W Vektörü:", self.in_W)
        
        self.btn_run = QPushButton("Hesapla")
        self.btn_run.clicked.connect(self.run_adjustment)
        self.out_res = QTextEdit(); self.out_res.setReadOnly(True)
        
        layout.addLayout(form)
        layout.addWidget(self.btn_run)
        layout.addWidget(self.out_res)
        self.setLayout(layout)
        
    def run_adjustment(self):
        try:
            n1 = int(self.in_ilk.toPlainText())
            n2 = int(self.in_ikinci.toPlainText())
            sig = float(self.in_sig.toPlainText())
            A = self.in_A.get_matrix()
            W = self.in_W.get_matrix()
            
            solver = pd2.Direkt_AdimAdim_Cozum_Trilaterasyon(n1, n2, A, W, sig)
            sonuc = solver.birliteDeltaCapSon()
            
            self.out_res.setPlainText(f"Sonuç (Delta Hatası):\n{np.array2string(sonuc, precision=4)}")
        except Exception as e:
            QMessageBox.critical(self, "Hata", str(e))

# --- MODÜL 3: KALMAN FİLTRESİ SEKME ---
class KalmanTab(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()
        
        # --- Sol: Ayarlar ---
        settings_group = QGroupBox("Kalman Ayarları (Sabit Hız)")
        form = QFormLayout()
        
        # Varsayılanlar 2D Hareket için (X, Y, Vx, Vy)
        self.combo_model = QComboBox()
        self.combo_model.addItems(["sabit_hiz", "sabit_ivme"])
        
        self.in_dt = QTextEdit("1.0"); self.in_dt.setMaximumHeight(25)
        self.in_x0 = MatrixInput("0; 0; 10; 5") # x=0, y=0, vx=10, vy=5
        self.in_Cr_val = QTextEdit("5.0"); self.in_Cr_val.setMaximumHeight(25) # Ölçüm Gürültüsü
        self.in_Ce_val = QTextEdit("0.1"); self.in_Ce_val.setMaximumHeight(25) # Sistem Gürültüsü
        
        # Simülasyon Verisi (Sadece Ölçümler: X ve Y)
        self.in_measurements = MatrixInput("") 
        self.btn_sim = QPushButton("Rastgele Rota Üret")
        self.btn_sim.clicked.connect(self.generate_simulation_data)
        
        form.addRow("Model Tipi:", self.combo_model)
        form.addRow("Zaman Adımı (dt):", self.in_dt)
        form.addRow("Başlangıç Durumu (x0):", self.in_x0)
        form.addRow("Ölçüm Gürültüsü (R):", self.in_Cr_val)
        form.addRow("Sistem Gürültüsü (Q):", self.in_Ce_val)
        form.addRow("Ölçümler (L):", self.in_measurements)
        
        self.btn_run = QPushButton("Kalman Filtresini Çalıştır")
        self.btn_run.clicked.connect(self.run_kalman)
        
        settings_group.setLayout(form)
        settings_group.layout().addWidget(self.btn_sim)
        settings_group.layout().addWidget(self.btn_run)
        
        # --- Sağ: Grafik ---
        self.canvas = MplCanvas(self)
        
        layout.addWidget(settings_group, 35)
        layout.addWidget(self.canvas, 65)
        self.setLayout(layout)

    def generate_simulation_data(self):
        """Kullanıcı elle girmesin diye sentetik veri üretir."""
        dt = float(self.in_dt.toPlainText())
        steps = 50
        # Gerçek Rota (Sabit Hız + Biraz sapma)
        true_x = np.linspace(0, 100, steps)
        true_y = 0.5 * true_x + 10 * np.sin(true_x * 0.1) # Biraz dalgalı yol
        
        # Gürültü Ekle
        noise = np.random.normal(0, 2.5, (steps, 2)) # 2.5m hata
        meas_x = true_x + noise[:, 0]
        meas_y = true_y + noise[:, 1]
        
        # Matris formatına çevir (String)
        data_str = ""
        for mx, my in zip(meas_x, meas_y):
            data_str += f"{mx:.2f}, {my:.2f}; "
        self.in_measurements.setPlainText(data_str.strip("; "))

    def run_kalman(self):
        try:
            # 1. Hazırlık
            dt = float(self.in_dt.toPlainText())
            model = self.combo_model.currentText()
            x_curr = self.in_x0.get_matrix().flatten() # (4,) vektör
            n_state = len(x_curr)
            
            # Kovaryanslar
            r_val = float(self.in_Cr_val.toPlainText())
            q_val = float(self.in_Ce_val.toPlainText())
            
            # Başlangıç Kovaryansı (Büyük belirsizlik)
            Cx_curr = np.eye(n_state) * 100 
            delta_curr = np.zeros(n_state) # İlk düzeltme sıfır
            
            # Ölçümler (N x 2 matrisi)
            L_data = self.in_measurements.get_matrix() 
            
            # Sabit Hız Modeli için Matrisler (Senin koduna uygun)
            # Senin Kalman sınıfın model tipini string olarak alıp S matrisini içeride kuruyor.
            # Ancak A (Design Matrix) ve Cr, Ce dışarıdan verilmeli.
            
            # A Matrisi: Durum vektöründen (x, y, vx, vy) -> Ölçüme (x, y) geçiş
            # Ölçüm sadece Konum (X, Y) ise:
            if n_state == 4: # 2D Sabit Hız
                A = np.array([[1, 0, 0, 0],
                              [0, 1, 0, 0]])
                Cr = np.eye(2) * (r_val**2)
            else:
                raise ValueError("Bu demo sadece 4 durumlu (x,y,vx,vy) 2D Sabit Hız için ayarlandı.")
                
            # Ce (Sistem Gürültüsü) - Genellikle S matrisi ile ilişkilidir ama burada basit tutuyoruz
            Ce = np.eye(n_state) * (q_val**2)
            
            kf = pd2.KalmanFiltresi(model_tipi=model)
            
            # --- 2. DÖNGÜ (LOOP) ---
            traj_estimated = []
            traj_measured = []
            
            for i in range(len(L_data)):
                L_curr = L_data[i] # Mevcut ölçüm (2, )
                
                # Senin fonksiyonun imzası:
                # x_curr, Cx_curr, delta_curr, G, W, S, Cx_pred, x_pred, x_prev
                res = kf.adim_hesapla(
                    x_curr, Cx_curr, delta_curr, 
                    L_curr, dt, A, Cr, Ce
                )
                
                # Güncellemeleri al
                x_curr = res[0]
                Cx_curr = res[1]
                delta_curr = res[2]
                
                # Sonuçları kaydet (Sadece Konum X, Y)
                traj_estimated.append([x_curr[0], x_curr[1]])
                traj_measured.append(L_curr)
            
            traj_estimated = np.array(traj_estimated)
            traj_measured = np.array(traj_measured)
            
            # --- 3. Çizim ---
            self.canvas.axes.cla()
            self.canvas.axes.scatter(traj_measured[:,0], traj_measured[:,1], c='red', s=10, label='Gürültülü Ölçüm', alpha=0.5)
            self.canvas.axes.plot(traj_estimated[:,0], traj_estimated[:,1], 'b-', linewidth=2, label='Kalman Filtresi')
            
            self.canvas.axes.set_title("Kalman Filtresi: Yörünge Takibi")
            self.canvas.axes.set_xlabel("X Konumu (m)")
            self.canvas.axes.set_ylabel("Y Konumu (m)")
            self.canvas.axes.legend()
            self.canvas.axes.grid(True)
            self.canvas.draw()
            
        except Exception as e:
            QMessageBox.critical(self, "Kalman Hatası", f"Detay:\n{str(e)}\n\nİpucu: Boyutlar uyuşmuyor olabilir.")


# --- ANA PENCERE ---
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bilimsel Jeodezik Hesaplama Platformu v2.0")
        self.resize(1100, 800)
        
        self.tabs = QTabWidget()
        
        self.tab_kollokasyon = KollokasyonTab()
        self.tab_adimadim = AdimAdimTab()
        self.tab_kalman = KalmanTab() # YENİ EKLENEN SEKME
        
        self.tabs.addTab(self.tab_kalman, "Kalman Filtresi (Yörünge)")
        self.tabs.addTab(self.tab_kollokasyon, "Kollokasyon")
        self.tabs.addTab(self.tab_adimadim, "Adım Adım Dengeleme")
        
        self.setCentralWidget(self.tabs)
        self.statusBar().showMessage("Sistem Hazır. Modüller: Kalman, Kollokasyon, Dengeleme")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())