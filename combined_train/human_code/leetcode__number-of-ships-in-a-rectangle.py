class C1(object):

    def hasShips(self, a1, a2):
        """
       """
        pass

class C2(object):

    def __init__(self, a1, a2):
        self.x = a1
        self.y = a2

class C3(object):

    def countShips(self, a1, a2, a3):
        """
        """
        v1 = 0
        if a2.x >= a3.x and a2.y >= a3.y and a1.hasShips(a2, a3):
            if (a2.x, a2.y) == (a3.x, a3.y):
                return 1
            v2, v3 = ((a2.x + a3.x) // 2, (a2.y + a3.y) // 2)
            v1 += self.countShips(a1, a2, C2(v2 + 1, v3 + 1))
            v1 += self.countShips(a1, C2(v2, a2.y), C2(a3.x, v3 + 1))
            v1 += self.countShips(a1, C2(a2.x, v3), C2(v2 + 1, a3.y))
            v1 += self.countShips(a1, C2(v2, v3), a3)
        return v1
