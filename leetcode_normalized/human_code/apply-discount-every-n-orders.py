class C1(object):

    def __init__(self, a1, a2, a3, a4):
        """
        """
        self.__n = a1
        self.__discount = a2
        self.__curr = 0
        self.__lookup = {p: a4[i] for v1, v2 in enumerate(a3)}

    def getBill(self, a1, a2):
        """
        """
        self.__curr = (self.__curr + 1) % self.__n
        v1 = 0.0
        for v2, v3 in enumerate(a1):
            v1 += self.__lookup[v3] * a2[v2]
        return v1 * (1.0 - self.__discount / 100.0 if self.__curr == 0 else 1.0)
