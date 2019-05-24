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
        self.titre.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#9c393b;\">Paint Ball V1</span></p></body></html>')

        self.jouer = QtWidgets.QPushButton('Jouer')
        self.jouer.setFont(font)

        # create frame for a set of radio button
        self.frameMode = QtWidgets.QFrame(self)

        self.radioBtnAleatoire = QtWidgets.QRadioButton("Génération aléatoire", self.frameMode)
        self.radioBtnAleatoire.setChecked(True)  # select by default
        self.radioBtnAleatoire.setFont(font)
        self.radioBtnMap = QtWidgets.QRadioButton("Cartes enregistrées", self.frameMode)
        self.radioBtnMap.setFont(font)
        self.radioBtnMap.move(240, 0)
        self.radioBtnAleatoire.clicked.connect(self.switch_mode)
        self.radioBtnMap.clicked.connect(self.switch_mode)


        # Si aléatoire

        self.aleatoireWidget = QtWidgets.QHBoxLayout()

        label_level = QtWidgets.QLabel('Level : ')
        label_level.setFont(font)

        self.level = QtWidgets.QSlider()
        self.level.setValue(12)
        self.level.setMinimum(3)
        self.level.setMaximum(20)
        self.level.setOrientation(QtCore.Qt.Horizontal)
        self.level.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.level.setTickInterval(1)

        self.aleatoireWidget.addWidget(label_level)
        self.aleatoireWidget.addWidget(self.level)

        # Si cartes enregistrées

        self.mapWidget = QtWidgets.QHBoxLayout()

        self.leftB = QtWidgets.QLabel('<-', self.frameSelection)
        self.map_name = QtWidgets.QLabel('Map XXX', self.frameSelection)
        self.rightB = QtWidgets.QLabel('->', self.frameSelection)

        self.mapWidget.addWidget(self.leftB)
        self.mapWidget.addWidget(self.map_name)
        self.mapWidget.addWidget(self.rightB)

        # stacking

        self.stackSelection = QtWidgets.QStackedLayout(self)
        self.stackSelection.addWidget(self.aleatoireWidget)
        self.stackSelection.addWidget(self.mapWidget)
        self.stackSelection.setCurrentIndex(0)





        spacer = QtWidgets.QSpacerItem(20, 40)

        layout.addWidget(self.titre)
        layout.addWidget(self.frameMode)
        layout.addWidget(label_level)
        layout.addWidget(self.level)
        layout.addItem(spacer)
        layout.addWidget(self.jouer)
        self.setLayout(layout)

    def switch_mode(self):
        print('I need to switch')
        #self.selectWidget.deleteLater()
        if self.radioBtnMap.isChecked():
            print('map')

        else:
            print('aléatoire')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    menu_ui = Ui_Menu()
    menu_ui.show()
    sys.exit(app.exec_())



