import math
import numpy as np
import random
import matplotlib.pyplot as plt
from PyQt5.QtCore import QPoint

class Map:
    def __init__(self, size=(700, 700), level=10):
        self.size = size
        #self.Qpolygone = []

        self.polygone = points = np.zeros((2, 0))

        self.arretes = []
        self.taches = [] # [[[Ax, Ay], [Bx, By]], [...], ...]

        self.startPoint = []
        self.finishPoint = []

    def generer(self, n=17, r_min=100, r_max=300):
        '''
        génération du polygone à découvrir
        :param n: nombre de points
        :param r_min: rayon min, tous les points seront a une distance supérieur du centre
        :param r_max: rayon max, tous les points seront a une distance inférieur du centre
        :return: matrice 2*n, coordonnées des points du polygone
        '''

        angles = sorted([random.random()*2*np.pi for i in range(n)])
        rayons = [random.random()*(r_max - r_min)+r_min for i in range(n)]

        points = np.zeros((2, n))

        for i in range(n):
            x = self.size[0]/2 + rayons[i]*np.cos(angles[i])
            y = self.size[1]/2 + rayons[i]*np.sin(angles[i])
            self.Qpolygone.append(QPoint(x, y))
            points[0, i] = x
            points[1, i] = y

        #print(points)
        #plt.plot(points[0, :], points[1, :])
        #plt.show()

        return points


