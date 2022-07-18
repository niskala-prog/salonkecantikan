import sys
from PyQt5 import QtWidgets, uic
import psycopg2 as mc
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtWidgets import QMessageBox
from classes.Alumni import Alumni

qtcreator_file  = "ui/alumni.ui" # Enter file here.
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)


class AlumniWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Event Setup
        self.btnCari.clicked.connect(self.search_data) # Jika tombol cari diklik
        self.btnSimpan.clicked.connect(self.save_data) # Jika tombol simpan diklik
        self.txtkode.returnPressed.connect(self.search_data) # Jika menekan tombol Enter saat berada di textbox kode
        self.btnClear.clicked.connect(self.clear_entry)
        self.btnHapus.clicked.connect(self.delete_data)
        self.edit_mode=""   
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def select_data(self):
        try:
            alum = Alumni()

            # Get all 
            result = alum.getAllData()

            self.gridAlumni.setHorizontalHeaderLabels(['ID', 'Kode Alumni', 'Nama', 'Jenis Kelamin', 'Tahun Lulus'])
            self.gridAlumni.setRowCount(0)
            

            for row_number, row_data in enumerate(result):
                #print(row_number)
                self.gridAlumni.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.gridAlumni.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def search_data(self):
        try:           
            kode=self.txtkode.text()           
            alum = Alumni()

            # search process
            result = alum.getBykode_alumni(kode)
            a = alum.affected
            if(a>0):
                self.TampilData(result)
            else:
                self.messagebox("INFO", "Data tidak ditemukan")
                self.txtNama.setFocus()
                self.btnSimpan.setText("Simpan")
                self.edit_mode=False
                self.btnHapus.setEnabled(False) # Matikan tombol hapus
                self.btnHapus.setStyleSheet("color:black;background-color : grey")
            
        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def save_data(self, MainWindow):
        try:
            alum = Alumni()
            kode=self.txtkode.text()
            nama=self.txtNama.text()
            if self.optLaki.isChecked():
                jk="L"
            
            if self.optPerempuan.isChecked():
                jk="P"

            tahun=self.txtTahun.text()
            
            if(self.edit_mode==False):   
                alum.kode_alumni = kode
                alum.nama = nama
                alum.jk = jk
                alum.tahun_lulus = tahun
                a = alum.simpan()
                if(a>0):
                    self.messagebox("SUKSES", "Data Alumni Tersimpan")
                else:
                    self.messagebox("GAGAL", "Data Alumni Gagal Tersimpan")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            elif(self.edit_mode==True):
                alum.nama = nama
                alum.jk = jk
                alum.tahun_lulus = tahun
                a = alum.updateBykode_alumni(kode)
                if(a>0):
                    self.messagebox("SUKSES", "Data Alumni Diperbarui")
                else:
                    self.messagebox("GAGAL", "Data Alumni Gagal Diperbarui")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Terjadi kesalahan Mode Edit")
            

        except mc.Error as e:
            self.messagebox("ERROR", str(e))

    def delete_data(self, MainWindow):
        try:
            alum = Alumni()
            kode=self.txtkode.text()
                       
            if(self.edit_mode==True):
                a = alum.deleteBykode_alumni(kode)
                if(a>0):
                    self.messagebox("SUKSES", "Data Alumni Dihapus")
                else:
                    self.messagebox("GAGAL", "Data Alumni Gagal Dihapus")
                
                self.clear_entry(self) # Clear Entry Form
                self.select_data() # Reload Datagrid
            else:
                self.messagebox("ERROR", "Sebelum meghapus data harus ditemukan dulu")
            

        except mc.Error as e:
            self.messagebox("ERROR", "Terjadi kesalahan koneksi data")

    def TampilData(self,result):
        self.txtkode.setText(result[1])
        self.txtNama.setText(result[2])
        if(result[3]=="L"):
            self.optLaki.setChecked(True)
            self.optPerempuan.setChecked(False)
        else:
            self.optLaki.setChecked(False)
            self.optPerempuan.setChecked(True)

        self.txtTahun.setText(result[4])
        self.btnSimpan.setText("Update")
        self.edit_mode=True
        self.btnHapus.setEnabled(True) # Aktifkan tombol hapus
        self.btnHapus.setStyleSheet("background-color : red")

    def clear_entry(self, MainWindow):
        self.txtkode.setText("")
        self.txtNama.setText("")
        self.optLaki.setChecked(False)
        self.optPerempuan.setChecked(False)
        self.txtTahun.setText("")
        self.btnHapus.setEnabled(False) # Matikan tombol hapus
        self.btnHapus.setStyleSheet("color:black;background-color : grey")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = AlumniWindow()
    window.show()
    window.select_data()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = AlumniWindow()