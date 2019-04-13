import math
import numpy as np
import random

class Map:
    def __init__(self):
        self.size = (10, 10)
        self.polygone = []

    def generer(self, n, r_min, r_max):
        self.angles = sorted([random.randint(0, 2*np.pi) for i in range(n)])
        print(self.angles)


