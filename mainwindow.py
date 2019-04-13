# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets
import model
import sys

class Ui_MainWindow(object):

    def __init__(self):
        self.model = model.Model()

        super().__init__()

    def afficher_polygone(self):
        self.polygone = QtGui.QPolygonF()
        points = self.model.map.polygone
        n = points.shape[1]
        for i in range(n):
            print('x : ', points[0, i], '/ y : ', points[1, i])
            self.polygone.append(QtCore.QPointF(points[0, i], points[1, i]))

    def mousePressEvent(self, event):
        print("appui souris")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setMinimumSize(QtCore.QSize(700, 700))
        self.centralWidget.setMaximumSize(QtCore.QSize(800, 800))
        self.centralWidget.setBaseSize(QtCore.QSize(700, 700))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.centralWidget.setFont(font)
        self.centralWidget.setStyleSheet("background : rgb(0, 0, 0)")
        self.centralWidget.setObjectName("centralWidget")
        self.pseudo = QtWidgets.QLabel(self.centralWidget)
        self.pseudo.setGeometry(QtCore.QRect(10, 0, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.pseudo.setFont(font)
        self.pseudo.setObjectName("pseudo")
        self.compteur_tir = QtWidgets.QLabel(self.centralWidget)
        self.compteur_tir.setGeometry(QtCore.QRect(120, 0, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        self.compteur_tir.setFont(font)
        self.compteur_tir.setObjectName("compteur_tir")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pseudo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt; color:#ffffff;\">Pseudo</span></p></body></html>"))
        self.compteur_tir.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; color:#ffffff;\">0</span></p></body></html>"))



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    principale_ihm = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(principale_ihm)
    principale_ihm.show()
    sys.exit(app.exec_())