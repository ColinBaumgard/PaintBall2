from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel


from PyQt5.QtGui import QPainter, QBrush, QPen, QPolygon, QIcon, QPixmap
from PyQt5.QtCore import Qt, QPoint, QTimer

import model
import collision
import map

import sys
import numpy as np
import time


class Editor(QMainWindow):

    def __init__(self, size=(1000, 1000)):
        super().__init__()

        self.geometrie = collision.Collision()
        self.x_mouse, self.y_mouse = 0, 0

        self.size = size
        self.fps = 60
        self.map = map.Map(self.size, 0)
        self.map.startPoint, self.map.finishPoint = QPoint(-100, -100), QPoint(-100, -100)
        self.poly = []
        self.distance_min = 20


        self.mode_edition = 0

        self.style_base = QPen(Qt.white, 2, Qt.SolidLine)
        self.style_gris = QPen(Qt.gray, 2, Qt.SolidLine)
        self.style_fin = QPen(Qt.red, 2, Qt.SolidLine)
        self.style_rouge = QPen(Qt.red, 4, Qt.SolidLine)

        self.initWindow()


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000 / self.fps)


    def initWindow(self):

        self.setMouseTracking(True)
        #self.setCursor(QtGui.QCursor(Qt.BlankCursor))
        self.setWindowTitle('Map Editor')
        self.setGeometry(200, 200, self.size[0], self.size[1])

        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setPalette(p)

        self.show()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(self.style_base)

        if self.mode_edition == 0:
            n = len(self.poly)
            if n > 0:
                x, y = self.poly[-1]
                painter.setPen(self.style_base)
                painter.drawLine(QPoint(x, y), QPoint(self.x_mouse, self.y_mouse))

                x0, y0 = self.poly[0]
                painter.drawEllipse(QPoint(x0, y0), self.distance_min, self.distance_min)

            if n > 1:
                for i in range(n - 1):
                    painter.setPen(self.style_base)
                    painter.drawLine(self.poly[i][0], self.poly[i][1], self.poly[(i+1)][0], self.poly[(i+1)][1])

        if self.mode_edition != 0:
            points = self.map.Qpolygone

            Qpoly = QPolygon(points)
            painter.setPen(self.style_gris)
            painter.drawPolygon(Qpoly)
            painter.setPen(self.style_base)

            painter.setPen(self.style_gris)
            painter.drawEllipse(self.map.startPoint, 2*self.distance_min, 2*self.distance_min)
            painter.setPen(self.style_rouge)
            painter.drawEllipse(self.map.finishPoint, 2*self.distance_min, 2*self.distance_min)





    def mousePressEvent(self, e):

        n = len(self.poly)
        A = e.x(), e.y()

        if self.mode_edition == 0:

            draw = True
            for point in self.poly:
                if self.geometrie.distanceAB(A, point) < self.distance_min:
                    draw = False
            if draw:
                self.poly.append(A)
            elif n > 2:
                if self.geometrie.distanceAB(A, self.poly[0]) < self.distance_min:
                    self.map.Qpolygone = [QPoint(A[0], A[1]) for A in self.poly]
                    self.mode_edition = 1

        if self.mode_edition == 1:
            self.map.startPoint = QPoint(self.x_mouse, self.y_mouse)

        elif self.mode_edition == 2:
            self.map.finishPoint = QPoint(self.x_mouse, self.y_mouse)




        self.update()

    def mouseMoveEvent(self, e):
        self.x_mouse, self.y_mouse = e.x(), e.y()

    def keyPressEvent(self, event):
        '''
        if key == Qt.Key_p:
            self.mode_edition = 0
        elif key == Qt.Key_l:
            self.mode_edition = 1
        elif key = Qt.Key_'''
        key = event.key()
        print(key)
        if key == Qt.Key_Execute:
            self.mode_edition += 1


if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    fen = Editor()

    sys.exit(app.exec())