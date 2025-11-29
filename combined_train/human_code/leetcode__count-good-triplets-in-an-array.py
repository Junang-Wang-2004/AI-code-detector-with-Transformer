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

    def goodTriplets(self, a1, a2):
        """
        """
        v1 = [0] * len(a1)
        for v2, v3 in enumerate(a1):
            v1[v3] = v2
        v4 = 0
        v5 = C1(len(a1))
        for v2, v3 in enumerate(a2):
            v6 = v5.query(v1[v3] - 1)
            v7 = len(a1) - (v1[v3] + 1) - (v2 - v6)
            v4 += v6 * v7
            v5.add(v1[v3], 1)
        return v4
