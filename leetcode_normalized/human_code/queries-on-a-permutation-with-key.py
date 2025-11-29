class C1(object):

    def __init__(self, a1):
        self.__bit = [0] * a1

    def add(self, a1, a2):
        while a1 < len(self.__bit):
            self.__bit[a1] += a2
            a1 += a1 & -a1

    def sum(self, a1):
        v1 = 0
        while a1 > 0:
            v1 += self.__bit[a1]
            a1 -= a1 & -a1
        return v1

class C2(object):

    def processQueries(self, a1, a2):
        """
        """
        v1 = C1(2 * a2 + 1)
        v2 = {}
        for v3 in range(1, a2 + 1):
            v1.add(a2 + v3, 1)
            v2[v3] = a2 + v3
        v4, v5 = ([], a2)
        for v6 in a1:
            v3 = v2.pop(v6)
            v4.append(v1.sum(v3 - 1))
            v1.add(v3, -1)
            v2[v6] = v5
            v1.add(v5, 1)
            v5 -= 1
        return v4
