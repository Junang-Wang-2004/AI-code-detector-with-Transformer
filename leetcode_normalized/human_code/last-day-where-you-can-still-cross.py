class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.rank = [0] * a1

    def find_set(self, a1):
        v1 = []
        while self.set[a1] != a1:
            v1.append(a1)
            a1 = self.set[a1]
        while v1:
            self.set[v1.pop()] = a1
        return a1

    def union_set(self, a1, a2):
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 == v2:
            return False
        if self.rank[v1] < self.rank[v2]:
            self.set[v1] = v2
        elif self.rank[v1] > self.rank[v2]:
            self.set[v2] = v1
        else:
            self.set[v2] = v1
            self.rank[v1] += 1
        return True

class C2(object):

    def latestDayToCross(self, a1, a2, a3):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def index(a1, a2, a3):
            return a2 * a1 + a3
        v2, v3 = (a1 * a2, a1 * a2 + 1)
        v4 = C1(a1 * a2 + 2)
        v5 = [[False] * a2 for v6 in range(a1)]
        for v7 in reversed(range(len(a3))):
            v8, v9 = a3[v7]
            v8, v9 = (v8 - 1, v9 - 1)
            for v10, v11 in v1:
                v12, v13 = (v8 + v10, v9 + v11)
                if not (0 <= v12 < a1 and 0 <= v13 < a2 and v5[v12][v13]):
                    continue
                v4.union_set(index(a2, v8, v9), index(a2, v12, v13))
            if v8 == 0:
                v4.union_set(v2, index(a2, v8, v9))
            if v8 == a1 - 1:
                v4.union_set(v3, index(a2, v8, v9))
            if v4.find_set(v2) == v4.find_set(v3):
                return v7
            v5[v8][v9] = True
        return -1
