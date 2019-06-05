# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\xb\PycharmProjects\PaintBall2\menu\menu.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys, os


class Ui_Menu(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Menu')
        self.resize(500, 300)

        self.liste_maps = os.listdir('maps')
        self.i_map = 0

        self.setupUi()

    def setupUi(self):

        font = QtGui.QFont()
        font.setFamily("Fixedsys")
        font.setPointSize(14)

        title_font = QtGui.QFont()
        title_font.setFamily("Cooper Black")
        title_font.setPointSize(14)



        layout = QtWidgets.QVBoxLayout()

        titre = QtWidgets.QLabel('PaintBall')
        titre.setFont(title_font)
        titre.setText('<html><head/><body><p align=\"center\"><span style=\" font-size:26pt; font-weight:600; color:#9c393b;\">Paint Ball V2</span></p></body></html>')

        # radio bouton
        self.mode = QtWidgets.QWidget()
        layout_mode = QtWidgets.QHBoxLayout()
        self.radioBtnAleatoire = QtWidgets.QRadioButton("Génération aléatoire", self.mode)
        self.radioBtnAleatoire.setChecked(True)  # select by default
        #self.radioBtnAleatoire.setFont(font)
        self.radioBtnMap = QtWidgets.QRadioButton("Cartes enregistrées", self.mode)
        #self.radioBtnMap.setFont(font)
        self.radioBtnMap.move(240, 0)
        self.radioBtnAleatoire.clicked.connect(self.switch_mode)
        self.radioBtnMap.clicked.connect(self.switch_mode)
        layout_mode.addWidget(self.radioBtnAleatoire)
        layout_mode.addWidget(self.radioBtnMap)
        self.mode.setLayout(layout_mode)


        # Selection

        self.stack = QtWidgets.QStackedWidget()
        self.stack_auto = QtWidgets.QWidget()
        self.stack_save = QtWidgets.QWidget()
        self.stack_auto_ui(title_font)
        self.stack_save_ui(title_font)
        self.stack.addWidget(self.stack_save)
        self.stack.addWidget(self.stack_auto)

        self.stack.setCurrentIndex(1)

        # Boutons jouer et creation map

        widget_bouton = QtWidgets.QWidget()

        self.jouer = QtWidgets.QPushButton('Jouer')
        self.creer_map = QtWidgets.QPushButton('Creer une carte')
        layout_bouton = QtWidgets.QHBoxLayout()
        layout_bouton.addWidget(self.jouer)
        layout_bouton.addWidget(self.creer_map)

        widget_bouton.setLayout(layout_bouton)


        # on colle le tout

        layout.addWidget(titre)
        layout.addWidget(self.mode)
        layout.addWidget(self.stack)
        layout.addWidget(widget_bouton)

        self.setLayout(layout)

    def stack_auto_ui(self, font):
        layout = QtWidgets.QVBoxLayout()

        label_level = QtWidgets.QLabel('Level : ')
        #label_level.setFont(font)

        self.level = QtWidgets.QSlider()
        self.level.setValue(12)
        self.level.setMinimum(3)
        self.level.setMaximum(20)
        self.level.setOrientation(QtCore.Qt.Horizontal)
        self.level.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.level.setTickInterval(1)

        layout.addWidget(label_level)
        layout.addWidget(self.level)
        self.stack_auto.setLayout(layout)

    def stack_save_ui(self, font):
        layout = QtWidgets.QHBoxLayout()
        layout.setAlignment(QtCore.Qt.AlignCenter)

        self.leftB = QtWidgets.QPushButton('<-   ')
        self.leftB.setFont(font)
        self.map_name = QtWidgets.QLabel(self.liste_maps[self.i_map][:-4])
        self.map_name.setFont(font)
        self.rightB = QtWidgets.QPushButton('   ->')
        self.rightB.setFont(font)


        self.leftB.clicked.connect(self.switch_map_left)
        self.rightB.clicked.connect(self.switch_map_right)

        layout.addWidget(self.leftB)
        layout.addWidget(self.map_name)
        layout.addWidget(self.rightB)

        self.stack_save.setLayout(layout)

    def switch_mode(self):
        #self.selectWidget.deleteLater()
        if self.radioBtnMap.isChecked():
            self.stack.setCurrentIndex(0)

        else:
            self.stack.setCurrentIndex(1)

    def switch_map_left(self):

        self.liste_maps = os.listdir('maps')

        self.i_map = (self.i_map + 1) % len(self.liste_maps)

        self.map_name.setText(self.liste_maps[self.i_map][:-4])

    def switch_map_right(self):

        self.liste_maps = os.listdir('maps')

        self.i_map = (self.i_map - 1) % len(self.liste_maps)

        self.map_name.setText(self.liste_maps[self.i_map][:-4])







if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    menu_ui = Ui_Menu()
    menu_ui.show()
    sys.exit(app.exec_())



