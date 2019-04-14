

class Collision:

    def pointsToPara(self, A, B):
        a, b = 0, 0
        xa, ya = A
        xb, yb = B

        if xa - xb != 0:
            a = (yb - ya)/(xb - xa)
            b = ya - a*xa

        return a, b


    def intersection(self, d1, d2):
        '''
        retourne le point d'intersection entre d1 et d2
        :param d1: (a1, b1) tuple des paramètres de la droite
        :param d2: (a2, b2)
        :return: bool d'intersection, coords intersection
        '''

        a1, b1 = d1
        a2, b2 = d2

        if a1 == a2:
            return False, 0, 0

        else:
            x = (b2 - b1)/(a1 - a2)
            y = a1*x + b1
            return True, x, y

    def estEntreAetB(self, C, A, B):
        xa, ya = A
        xb, yb = B
        xc, yc = C

        if xc <= max(xa, xb) and xc >= min(xa, xb):
            if yc <= max(ya, yb) and yc >= min(ya, yb):
                return True
        return False





if __name__ == '__main__':
    col = Collision()
    print(col.intersection((1, 0), (-1, 2)))
    print(col.estEntreAetB((2, 2), (1, 1), (-3,-3)))