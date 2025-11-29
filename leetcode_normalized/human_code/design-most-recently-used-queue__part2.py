class C1(object):

    def __init__(self, a1):
        v1 = 2000
        self.__bit = [0] * (a1 + v1 + 1)
        for v2 in range(1, len(self.__bit)):
            self.__bit[v2] = (1 if v2 - 1 < a1 else 0) + self.__bit[v2 - 1]
        for v2 in reversed(range(1, len(self.__bit))):
            v3 = v2 - (v2 & -v2)
            self.__bit[v2] -= self.__bit[v3]

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

    def binary_lift(self, a1):
        v1 = (len(self.__bit) - 1).bit_length() - 1
        v2 = 2 ** v1
        v3 = v4 = 0
        for v5 in reversed(range(v1 + 1)):
            if v4 + v2 < len(self.__bit) and (not v3 + self.__bit[v4 + v2] >= a1):
                v3 += self.__bit[v4 + v2]
                v4 += v2
            v2 >>= 1
        return v4 + 1 - 1

class C2(object):

    def __init__(self, a1):
        """
        """
        self.__bit = C1(a1)
        self.__lookup = {i: i + 1 for v1 in range(a1)}
        self.__curr = a1

    def fetch(self, a1):
        """
        """
        v1 = self.__bit.binary_lift(a1)
        v2 = self.__lookup.pop(v1)
        self.__bit.add(v1, -1)
        self.__bit.add(self.__curr, 1)
        self.__lookup[self.__curr] = v2
        self.__curr += 1
        return v2
