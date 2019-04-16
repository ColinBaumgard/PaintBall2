# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\xb\PycharmProjects\PaintBall2\menu\menu.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_Menu(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Menu')
        self.resize(500, 300)

        self.setupUi()

    def setupUi(self):

        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(14)

        title_font = QtGui.QFont()
        title_font.setFamily("Cooper Black")
        title_font.setPointSize(14)

        layout =  QtWidgets.QGridLayout()

        self.titre = QtWidgets.QLabel('PaintBall')
        self.titre.setFont(title_font)
        self.titre.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#9c393b;\">Paint Ball V0.1</span></p></body></html>')

        self.jouer = QtWidgets.QPushButton('Jouer')
        self.jouer.setFont(font)

        label_level = QtWidgets.QLabel('Level : ')
        label_level.setFont(font)

        self.level = QtWidgets.QSlider()
        self.level.setMinimum(3)
        self.level.setMaximum(20)
        self.level.setOrientation(QtCore.Qt.Horizontal)
        self.level.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.level.setTickInterval(1)

        spacer = QtWidgets.QSpacerItem(20, 40)

        layout.addWidget(self.titre)
        layout.addWidget(label_level)
        layout.addWidget(self.level)
        layout.addItem(spacer)
        layout.addWidget(self.jouer)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    principale_ihm = QtWidgets.QMainWindow()
    ui = Ui_Menu()
    ui.setupUi(principale_ihm)
    principale_ihm.show()
    sys.exit(app.exec_())