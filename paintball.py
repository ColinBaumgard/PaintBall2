from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow


from PyQt5.QtGui import QPainter, QBrush, QPen, QPolygon
from PyQt5.QtCore import Qt, QPoint, QTimer

import model
import sys
import numpy as np


class Main(QMainWindow):

    def __init__(self):
        super().__init__()

        self.size = (700, 700)
        self.model = model.Model(self.size)
        self.r_player = 10
        self.r_deplacement = 100

        self.x_mouse, self.y_mouse = 0, 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(10)

        self.initWindow()

    def initWindow(self):

        self.setMouseTracking(True)
        self.setWindowTitle('PainBall')
        self.setGeometry(200, 200, self.size[0], self.size[1])

        self.show()

    def paintEvent(self, event):

        # etat joueur True = tir, False = deplacement
        etat = self.model.player.etat


        # affichage polygone
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        #painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))

        poly = self.model.map.polygone
        points = [QPoint(poly[0, i], poly[1, i]) for i in range(0, poly.shape[1])]
        #points = [QPoint(100, 100), QPoint(200, 100), QPoint(200, 100)]

        poly = QPolygon(points)
        painter.drawPolygon(poly)

        # affichage joueur
        xy = self.model.player.coords
        painter.drawEllipse(QPoint(xy[0], xy[1]), self.r_player, self.r_player)

        # affichage ligne si etat = tir = True
        if etat:
            a, b, s = self.pointsToParam()  # on récupère les infos pour avoir une demi-droite ( on prend un pt à l'exterieur, +/- 1000à
            painter.drawLine(xy[0], xy[1], 1000*s, a*1000*s + b)

        # affichage cercle deplacement
        else:
            painter.drawEllipse(QPoint(xy[0], xy[1]), self.r_deplacement, self.r_deplacement)


    def mousePressEvent(self, e):
        etat = self.model.player.etat
        self.model.player.etat = not etat

        if etat :  # ie si tir
            pass
        else:  # ie si deplacement
            self.model.player.coords = (e.x(), e.y(), 0)

        self.update()

    def mouseMoveEvent(self, e):
        self.x_mouse, self.y_mouse = e.x(), e.y()

    def setAngle(self):
        '''
        coords = self.model.player.coords
        dx, dy = self.x_mouse - coords[0], self.y_mouse - coords[1]
        if dy != 0:
            self.model.player.coords = (coords[0], coords[1], np.arctan(dx/dy))

        self.update()'''

    def pointsToParam(self):
        '''
        retourne les paramètres d'une droite ansi qu'une indication sur la direction de celle si
        :return: a, b de ax+n et s si la droite est vers la droite (+) ou vers la gauche (-)
        '''

        a, b, s = 0, 0, 0
        x, y, alpha = self.model.player.coords


        if self.x_mouse - x != 0:
            a = (self.y_mouse - y)/(self.x_mouse - x)
            b = y - a*x
            s = (self.x_mouse - x) / abs(self.x_mouse - x)


        return a, b, s





if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    fen = Main()

    sys.exit(app.exec())