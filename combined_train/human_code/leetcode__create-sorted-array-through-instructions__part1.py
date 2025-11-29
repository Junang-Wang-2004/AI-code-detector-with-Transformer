class C1(object):

    def __init__(self, a1):
        self.__bit = [0] * (a1 + 1)

    def add(self, a1, a2):
        a1 += 1
        while a1 < len(self.__bit):
            self.__bit[a1] += a2
            a1 += a1 & -a1

    def query(self, a1):
        a1 += 1
        v2 = 0
        while a1 > 0:
            v2 += self.__bit[a1]
            a1 -= a1 & -a1
        return v2

class C2(object):

    def createSortedArray(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = C1(max(a1))
        v3 = 0
        for v4, v5 in enumerate(a1):
            v5 -= 1
            v3 += min(v2.query(v5 - 1), v4 - v2.query(v5))
            v2.add(v5, 1)
        return v3 % v1
