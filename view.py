import mainwindow

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class View:
    def __init__(self):
        self.init_window()


    def init_window(self):
        app = QtWidgets.QApplication(sys.argv)
        principale_ihm = QtWidgets.QMainWindow()
        ui = mainwindow.Ui_MainWindow()
        ui.setupUi(principale_ihm)
        principale_ihm.show()
        sys.exit(app.exec_())
