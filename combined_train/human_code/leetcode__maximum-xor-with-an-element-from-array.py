class C1(object):

    def __init__(self, a1):
        self.__root = {}
        self.__bit_length = a1

    def insert(self, a1):
        v1 = self.__root
        for v2 in reversed(range(self.__bit_length)):
            v3 = a1 >> v2 & 1
            if v3 not in v1:
                v1[v3] = {}
            v1 = v1[v3]

    def query(self, a1):
        if not self.__root:
            return -1
        v1, v2 = (self.__root, 0)
        for v3 in reversed(range(self.__bit_length)):
            v4 = a1 >> v3 & 1
            if 1 ^ v4 in v1:
                v1 = v1[1 ^ v4]
                v2 |= 1 << v3
            else:
                v1 = v1[v4]
        return v2

class C2(object):

    def maximizeXor(self, a1, a2):
        """
        """
        a1.sort()
        v1 = max(a1[-1], max(a2, key=lambda x: x[0])[0])
        a2 = sorted(enumerate(a2), key=lambda x: x[1][1])
        v3 = C1(v1.bit_length())
        v4 = [-1] * len(a2)
        v5 = 0
        for v6, (v7, v8) in a2:
            while v5 < len(a1) and a1[v5] <= v8:
                v3.insert(a1[v5])
                v5 += 1
            v4[v6] = v3.query(v7)
        return v4
