from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow


from PyQt5.QtGui import QPainter, QBrush, QPen, QPolygon
from PyQt5.QtCore import Qt, QPoint

import model
import sys



class Main(QMainWindow):
    def __init__(self):
        super().__init__()

        self.size = (700, 700)
        self.model = model.Model(self.size)

        self.initWindow()

    def initWindow(self):

        self.setWindowTitle('PainBall')
        self.setGeometry(200, 200, self.size[0], self.size[1])

        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))

        poly = self.model.map.polygone
        points = [QPoint(poly[0, i], poly[1, i]) for i in range(0, poly.shape[1])]
        #points = [QPoint(100, 100), QPoint(200, 100), QPoint(200, 100)]

        poly = QPolygon(points)
        painter.drawPolygon(poly)

    def mousePressEvent(self, e):
        print("OK")


    def afficher_polygone(self):
        polygone = QtGui.QPolygonF()
        points = self.model.map.polygone
        n = points.shape[1]
        for i in range(n):
            print('x : ', points[0, i], '/ y : ', points[1, i])
            polygone.append(QtCore.QPointF(points[0, i] + self.size[0]/2, points[1, i] + self.size[1]/2))


    def draw(self, qp, event):

        qp.setPen(QtGui.QColor(168, 34, 3))
        qp.setFont(QtGui.QFont('Decorative', 10))
        qp.drawText(event.rect(), QtCore.Qt.AlignCenter, self.text)




if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    fen = Main()

    sys.exit(app.exec())