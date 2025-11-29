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

    def pancakeSort(self, a1):
        """
        """
        v1 = C1(len(a1))
        v2 = []
        for v3 in range(len(a1)):
            v4 = v1.query(a1[v3] - 1 - 1)
            v1.add(a1[v3] - 1, 1)
            if v4 == v3:
                continue
            if v4 == 0:
                if v3 > 1:
                    v2.append(v3)
                v2.append(v3 + 1)
            else:
                if v4 > 1:
                    v2.append(v4)
                v2.append(v3)
                v2.append(v3 + 1)
                v2.append(v4 + 1)
        return v2
