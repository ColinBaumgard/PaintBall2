from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QInputDialog, QLineEdit


from PyQt5.QtGui import QPainter, QBrush, QPen, QPolygon, QIcon, QPixmap
from PyQt5.QtCore import Qt, QPoint, QTimer

import model
import collision
import map

import sys
import pickle
import numpy as np
import time


class Editor(QMainWindow):

    def __init__(self, size=(700, 700)):
        super().__init__()

        self.geometrie = collision.Collision()
        self.x_mouse, self.y_mouse = 0, 0

        self.size = size
        self.fps = 60
        self.map = map.Map(self.size, 0)
        self.map.startPoint, self.map.finishPoint = QPoint(-100, -100), QPoint(-100, -100)
        self.poly = []
        self.distance_min = 20
        self.title = 'untitled'
        self.mode_edition = 0
        self.distance_selection = 20

        self.selectedPoint = (False, 0)


        self.style_base = QPen(Qt.white, 2, Qt.SolidLine)
        self.style_gris = QPen(Qt.gray, 2, Qt.SolidLine)
        self.style_fin = QPen(Qt.red, 2, Qt.SolidLine)
        self.style_rouge = QPen(Qt.red, 4, Qt.SolidLine)
        self.style_vert = QPen(Qt.green, 2, Qt.SolidLine)
        self.style_jaune = QPen(Qt.yellow, 2, Qt.SolidLine)

        title_font = QtGui.QFont()
        title_font.setFamily("Cooper Black")
        title_font.setPointSize(14)

        self.initWindow()


        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000 / self.fps)


    def initWindow(self):

        self.setMouseTracking(True)
        #self.setCursor(QtGui.QCursor(Qt.BlankCursor))
        self.setWindowTitle('Map Editor')
        self.setGeometry(50, 50, self.size[0], self.size[1])

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

            painter.setPen(self.style_jaune)
            painter.drawEllipse(self.map.startPoint, 2*self.distance_min, 2*self.distance_min)

            painter.setPen(self.style_vert)
            painter.drawEllipse(self.map.finishPoint, 2*self.distance_min, 2*self.distance_min)

        if self.mode_edition == 0:
            painter.setPen(self.style_base)
            painter.drawText(50, 100, ' - Tracez un polygone - ')
        elif self.mode_edition == 1:
            painter.setPen(self.style_jaune)
            painter.drawText(50, 100, ' - Placez un point de départ - ')
        elif self.mode_edition == 2:
            painter.setPen(self.style_vert)
            painter.drawText(50, 100, " - Placez un point d'arrivée - ")
        elif self.mode_edition == 3:
            painter.setPen(self.style_base)
            painter.drawText(50, 100, " - Appuyez sur entrée après modification eventuelle - ")
            for M in self.poly:
                painter.drawEllipse(QPoint(M[0], M[1]), self.distance_min, self.distance_min)



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
                    points = np.zeros((2, n))
                    for i in range(n):
                        points[0, i] = self.poly[i][0]
                        points[1, i] = self.poly[i][1]
                    self.map.polygone = points
                    self.mode_edition = 1

        elif self.mode_edition == 1:
            self.map.startPoint = QPoint(self.x_mouse, self.y_mouse)
            self.mode_edition = 2

        elif self.mode_edition == 2:
            self.map.finishPoint = QPoint(self.x_mouse, self.y_mouse)
            self.mode_edition = 3

        elif self.mode_edition == 3:
            i = 0
            self.selectedPoint = (False, 0)
            for M in self.poly:
                if self.geometrie.distanceAB(M, A) < self.distance_min:
                    self.selectedPoint = (True, i)
                i += 1

        self.update()

    def mouseReleaseEvent(self, *args, **kwargs):
        if self.mode_edition == 3:
            self.selectedPoint = (False, 0)

    def mouseMoveEvent(self, e):
        self.x_mouse, self.y_mouse = e.x(), e.y()

        if self.mode_edition == 1:
            self.map.startPoint = QPoint(self.x_mouse, self.y_mouse)

        elif self.mode_edition == 2:
            self.map.finishPoint = QPoint(self.x_mouse, self.y_mouse)

        elif self.mode_edition == 3 and self.selectedPoint[0]:
            QM = QPoint(self.x_mouse, self.y_mouse)
            M = (self.x_mouse, self.y_mouse)
            self.poly[self.selectedPoint[1]] = M
            self.map.polygone[0, self.selectedPoint[1]] = self.x_mouse
            self.map.polygone[1, self.selectedPoint[1]] = self.y_mouse
            self.map.Qpolygone[self.selectedPoint[1]] = QM


    def keyPressEvent(self, event):
        '''
        if key == Qt.Key_p:
            self.mode_edition = 0
        elif key == Qt.Key_l:
            self.mode_edition = 1
        elif key = Qt.Key_'''
        key = event.key()
        #print(key)
        if key == Qt.Key_Return and self.mode_edition == 3:
            print('enter')
            self.getText()

    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Map Editor", "Nom de la map :", QLineEdit.Normal, "")
        if okPressed and text != '':
            self.title = text
            self.saveMap()
            self.destroy()

    def saveMap(self):
       # pickle.dump(self.map, open('maps/' + self.title + '.map', 'wb'))


        with open('maps/' + self.title + '.map', 'w') as file:
            file.write('s/{}/{}\n'.format(self.map.startPoint.x(), self.map.startPoint.y()))
            file.write('f/{}/{}\n'.format(self.map.finishPoint.x(), self.map.finishPoint.y()))

            for i in range(self.map.polygone.shape[1]):
                file.write('p/{}/{}\n'.format(self.map.polygone[0, i], self.map.polygone[1, i]))





if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    fen = Editor()

    sys.exit(app.exec())