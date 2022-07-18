import sys
from PyQt5.QtWidgets import *
# from forms.MainWindow import MainWindow
from forms.frmLogin import WindowLogin
__author__ = 'umc'

def main():
    a = QApplication(sys.argv)
    a.setQuitOnLastWindowClosed(True)
    login = WindowLogin()
    login.show()
    sys.exit(a.exec_())

main()