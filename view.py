import mainwindow
import model

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class View:
    def __init__(self):
        self.ui = self.init_window()


    def print(self, model):
        '''
        :param model: modèle du système
        '''

        self.ui.compteur_tir.setText = model.player.compteur_tir



    def init_window(self):
        '''initialise la fenêtre principale'''
        app = QtWidgets.QApplication(sys.argv)
        principale_ihm = QtWidgets.QMainWindow()
        ui = mainwindow.Ui_MainWindow()
        ui.setupUi(principale_ihm)
        principale_ihm.show()
        app.exec_()
        return ui
