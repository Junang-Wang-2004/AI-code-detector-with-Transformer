class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.count = a1

    def find_set(self, a1):
        if self.set[a1] != a1:
            self.set[a1] = self.find_set(self.set[a1])
        return self.set[a1]

    def union_set(self, a1, a2):
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 != v2:
            self.set[min(v1, v2)] = max(v1, v2)
            self.count -= 1

class C2(object):

    def regionsBySlashes(self, a1):
        """
        """

        def index(a1, a2, a3, a4):
            return (a2 * a1 + a3) * 4 + a4
        v1 = C1(len(a1) ** 2 * 4)
        v2, v3, v4, v5 = list(range(4))
        for v6 in range(len(a1)):
            for v7 in range(len(a1)):
                if v6:
                    v1.union_set(index(len(a1), v6 - 1, v7, v4), index(len(a1), v6, v7, v2))
                if v7:
                    v1.union_set(index(len(a1), v6, v7 - 1, v3), index(len(a1), v6, v7, v5))
                if a1[v6][v7] != '/':
                    v1.union_set(index(len(a1), v6, v7, v2), index(len(a1), v6, v7, v3))
                    v1.union_set(index(len(a1), v6, v7, v4), index(len(a1), v6, v7, v5))
                if a1[v6][v7] != '\\':
                    v1.union_set(index(len(a1), v6, v7, v5), index(len(a1), v6, v7, v2))
                    v1.union_set(index(len(a1), v6, v7, v3), index(len(a1), v6, v7, v4))
        return v1.count
