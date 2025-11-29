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
        if v1 == v2:
            return False
        self.set[max(v1, v2)] = min(v1, v2)
        self.count -= 1
        return True

class C2(object):

    def minCostToSupplyWater(self, a1, a2, a3):
        """
        """
        v1 = [[c, 0, i] for v2, v3 in enumerate(a2, 1)]
        v4 = [[v3, v2, j] for v2, v5, v3 in a3]
        v6 = 0
        v7 = C1(a1 + 1)
        for v3, v8, v9 in sorted(v1 + v4):
            if not v7.union_set(v8, v9):
                continue
            v6 += v3
            if v7.count == 1:
                break
        return v6
