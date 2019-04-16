from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow


from PyQt5.QtGui import QPainter, QBrush, QPen, QPolygon
from PyQt5.QtCore import Qt, QPoint, QTimer

import model
import collision

import sys
import numpy as np
import time


class Main(QMainWindow):

    def __init__(self, level=10):
        super().__init__()

        self.collision = collision.Collision()

        self.size = (700, 700)
        self.model = model.Model(self.size, level)
        self.r_player = 10
        self.r_deplacement = 100
        self.fps = 60

        self.tir = (0, 0, (False, 0, 0))  # angle, temps et impacte(bool, (i, j), r_min)
        self.v_tir = 500
        self.lg_tir = 20
        self.r_tir_max = 500

        self.deplacement = (0, (0, 0), 0) #  angle, distance target, t0 initial time

        self.x_mouse, self.y_mouse = 0, 0

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000/self.fps)

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

        for i in range(len(points)):
            painter.drawText(points[i], str(i))



        Qpoly = QPolygon(points)
        painter.setPen(QPen(Qt.gray, 2, Qt.SolidLine))
        painter.drawPolygon(Qpoly)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))

        # affichage arretes découvertes

        arretes = self.model.map.arretes
        for arrete in arretes:
            A = QPoint(poly[0, arrete[0]], poly[1, arrete[0]])
            B = QPoint(poly[0, arrete[1]], poly[1, arrete[1]])


            painter.drawLine(A, B)



        # affichage joueur
        xy = self.model.player.coords


        ###### affichage selon les differents état de jeu #####


        # Demande de tir : 0
        if etat == 0:
            self.demande_tir(painter)

        # Animation tir
        elif etat == 1:
            self.animation_tir(painter)

        # Demande de déplacement
        elif etat == 2:
            self.demande_deplacement(painter)

        # Animation déplacement
        elif etat == 3:
            self.animation_deplacement(painter)



        # Si il y a eu une erreur...
        else:
            self.model.player.etat = 0



    def mousePressEvent(self, e):
        etat = self.model.player.etat
        x_player, y_player, angle = self.model.player.coords
        #self.model.player.etat = (etat + 1) % 4

        if etat == 0:  # ie si tir
            self.model.player.etat = 1
            a = self.getAngle()
            impacte = self.collision_tir()
            self.tir = (a, time.time(), impacte)
            #self.animation_tir()

        elif etat == 2:  # ie si deplacement
            alpha = self.getAngle()
            distance = np.sqrt((e.x() - x_player)**2 + (e.y() - y_player)**2)
            self.deplacement = (alpha, distance, time.time())
            self.model.player.etat = 3

        self.update()


    def mouseMoveEvent(self, e):
        self.x_mouse, self.y_mouse = e.x(), e.y()


    def getAngle(self):
        '''
        retourne l'angle du joueur
        '''

        a, b, s = 0, 0, 0
        x, y, alpha = self.model.player.coords
        dx, dy = self.x_mouse - x, self.y_mouse - y

        if dx != 0 and dy != 0:
            s_1 = dx / abs(dx)
            s_2 = (dy) / abs(dy)
            alpha = np.arctan(dy / dx)
            if s_1 < 0:
                alpha += np.pi
            elif s_2 < 0:
                alpha += 2*np.pi
        elif dx == 0:
            if dy < 0:
                return 3*np.pi/2
            else:
                return np.pi/2
        else:
            if dx < 0:
                return np.pi
            else:
                return 0

        return alpha

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

    def collision_tir(self):

        xy = self.model.player.coords
        a1, b1, s = self.pointsToParam()
        d1 = (a1, b1)
        alpha = self.getAngle()

        poly = self.model.map.polygone
        n = poly.shape[1]
        impacte = (0, 0)

        r_min = 10000 #  valeur sortant de la fenêtre

        for i in range(n):

            j = (i+1) % n
            d2 = self.collision.pointsToPara((poly[0, i], poly[1, i]), (poly[0, j], poly[1, j]))
            point_coll = self.collision.intersection(d1, d2)

            if point_coll[0]:
                C = (point_coll[1], point_coll[2])
                r_sup = 10000
                x, y = xy[0] + r_sup * np.cos(alpha), xy[1] + r_sup * np.sin(alpha)
                if self.collision.estEntreAetB(C, (poly[0, i], poly[1, i]), (poly[0, j], poly[1, j])):
                    if self.collision.estEntreAetB(C, (xy[0], xy[1]), (x, y)):
                        print(i, j)
                        r = np.sqrt((point_coll[0] - xy[0])**2 + (point_coll[1] - xy[1])**2)
                        if r < r_min:
                            r_min = r
                            impacte = (i, j)


        if impacte != (0, 0):
            return True, impacte, r_min
        else:
            return False, impacte, r_min



    def demande_tir(self, painter):
        xy = self.model.player.coords
        alpha = self.getAngle()
        r_sup = 1000
        x, y = xy[0] + r_sup * np.cos(alpha), xy[1] + r_sup * np.sin(alpha)

        painter.drawEllipse(QPoint(xy[0], xy[1]), self.r_player, self.r_player)
        painter.drawLine(xy[0], xy[1], x, y)


    def animation_tir(self, painter):
        xy = self.model.player.coords
        alpha, t0, impacte = self.tir  # on récupère les infos pour avoir une demi-droite ( on prend un pt à l'exterieur, +/- 1000à
        if impacte[0]:
            r_tir_max = impacte[2]
        else:
            r_tir_max = self.r_tir_max
        t = time.time() - t0
        r_tir = t * self.v_tir
        x1, y1 = xy[0] + r_tir * np.cos(alpha), xy[1] + r_tir * np.sin(alpha)
        if r_tir < self.lg_tir:
            x2, y2 = xy[0], xy[1]
        else:
            h = self.lg_tir + r_tir  # hypothenus
            x2, y2 = xy[0] + h * np.cos(alpha), xy[1] + h * np.sin(alpha)
        if r_tir > r_tir_max:  # quand le tir touche un mur ou dépasse la limite du terrain, on passe à l'etat suivant
            if impacte[0]:
                if impacte[1] not in self.model.map.arretes:
                    self.model.map.arretes.append(impacte[1])
            self.model.player.etat = 2

        painter.drawEllipse(QPoint(xy[0], xy[1]), self.r_player, self.r_player)
        painter.drawLine(x1, y1, x2, y2)

    def animation_deplacement(self, painter):
        xy = self.model.player.coords
        alpha, distance, t0 = self.deplacement
        t = time.time() - t0
        r = self.model.player.vitesse * t
        x0, y0 = xy[0] + r * np.cos(alpha), xy[1] + r * np.sin(alpha)
        if r > min(distance, self.r_deplacement):
            self.model.player.coords = (x0, y0, alpha)
            self.model.player.etat = 0

        painter.drawEllipse(QPoint(xy[0], xy[1]), self.r_deplacement, self.r_deplacement)
        painter.drawEllipse(QPoint(x0, y0), self.r_player, self.r_player)

    def demande_deplacement(self, painter):
        xy = self.model.player.coords
        if np.sqrt((xy[0] - self.x_mouse) ** 2 + (xy[1] - self.y_mouse) ** 2) < self.r_deplacement:
            x, y = self.x_mouse, self.y_mouse
        else:
            alpha = self.getAngle()
            x, y = xy[0] + self.r_deplacement * np.cos(alpha), xy[1] + self.r_deplacement * np.sin(alpha)

        painter.drawEllipse(QPoint(xy[0], xy[1]), self.r_player, self.r_player)
        painter.drawLine(xy[0], xy[1], x, y)
        painter.drawEllipse(QPoint(xy[0], xy[1]), self.r_deplacement, self.r_deplacement)



if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    fen = Main()

    sys.exit(app.exec())