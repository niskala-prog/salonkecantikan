import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from forms.MainWindow import MainWindow
from classes.Users import Users as Login

qtcreator_file  = "ui/login.ui" # File Design Tampilan Dashboard
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtcreator_file)

class WindowLogin(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)     
        # Event Setup
        self.btnSubmit.clicked.connect(self.app_login) # ketika klik tombol submit
        
    def app_login(self):
        username = self.txtUsername.text()
        password = self.txtPassword.text()
        valid = usr.Validasi(username,password)
        #role = usr.rolename.strip()
        if(valid[0]==True): # Login berhasil   
            self.messagebox("Info","Login Berhasil")
            if(valid[1]=='admin'):
                self.messagebox("Info","Anda Login sebagai Admin")
                dashboard.showFullScreen()
            if(valid[1]=='pegawai'):
                self.messagebox("Info","Anda Login sebagai Pegawai")
                dashboard.showFullScreen()
            # close
            self.close()
        else: # login gagal
            self.messagebox("Info","Maaf login gagal")

    def messagebox(self, title, message):
        mess = QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QMessageBox.Ok)
        mess.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = WindowLogin() # load object window login
    dashboard = MainWindow() # load object window dashboard      
    window.show() # Tampilkan window login
    usr = Login()
    sys.exit(app.exec_())
else:
    app = QtWidgets.QApplication(sys.argv)
    window = WindowLogin() # load object window login
    dashboard = MainWindow() # load object window dashboard      
    usr = Login()