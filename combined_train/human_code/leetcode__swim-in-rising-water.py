class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))

    def find_set(self, a1):
        if self.set[a1] != a1:
            self.set[a1] = self.find_set(self.set[a1])
        return self.set[a1]

    def union_set(self, a1, a2):
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 == v2:
            return False
        self.set[min(v1, v2)] = max(v1, v2)
        return True

class C2(object):

    def swimInWater(self, a1):
        """
        """
        v1 = len(a1)
        v2 = [None] * v1 ** 2
        for v3 in range(v1):
            for v4 in range(v1):
                v2[a1[v3][v4]] = (v3, v4)
        v5 = ((-1, 0), (1, 0), (0, -1), (0, 1))
        v6 = C1(v1 ** 2)
        for v7 in range(v1 ** 2):
            v3, v4 = v2[v7]
            for v8 in v5:
                v9, v10 = (v3 + v8[0], v4 + v8[1])
                if 0 <= v9 < v1 and 0 <= v10 < v1 and (a1[v9][v10] <= v7):
                    v6.union_set(v3 * v1 + v4, v9 * v1 + v10)
                    if v6.find_set(0) == v6.find_set(v1 ** 2 - 1):
                        return v7
        return v1 ** 2 - 1
