class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1 + 1))
        self.size = [1] * (a1 + 1)
        self.size[-1] = 0

    def find_set(self, a1):
        if self.set[a1] != a1:
            self.set[a1] = self.find_set(self.set[a1])
        return self.set[a1]

    def union_set(self, a1, a2):
        v1, v2 = list(map(self.find_set, (a1, a2)))
        if v1 == v2:
            return False
        self.set[min(v1, v2)] = max(v1, v2)
        self.size[max(v1, v2)] += self.size[min(v1, v2)]
        return True

    def top(self):
        return self.size[self.find_set(len(self.size) - 1)]

class C2(object):

    def hitBricks(self, a1, a2):
        """
        """

        def index(a1, a2, a3):
            return a2 * a1 + a3
        v1 = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        v2, v3 = (len(a1), len(a1[0]))
        v4 = [row[:] for v5 in a1]
        for v6, v7 in a2:
            v4[v6][v7] = 0
        v8 = C1(v2 * v3)
        for v9, v5 in enumerate(v4):
            for v10, v11 in enumerate(v5):
                if not v11:
                    continue
                if v9 == 0:
                    v8.union_set(index(v3, v9, v10), v2 * v3)
                if v9 and v4[v9 - 1][v10]:
                    v8.union_set(index(v3, v9, v10), index(v3, v9 - 1, v10))
                if v10 and v4[v9][v10 - 1]:
                    v8.union_set(index(v3, v9, v10), index(v3, v9, v10 - 1))
        v12 = []
        for v9, v10 in reversed(a2):
            v13 = v8.top()
            if a1[v9][v10] == 0:
                v12.append(0)
                continue
            for v14 in v1:
                v15, v16 = (v9 + v14[0], v10 + v14[1])
                if 0 <= v15 < v2 and 0 <= v16 < v3 and v4[v15][v16]:
                    v8.union_set(index(v3, v9, v10), index(v3, v15, v16))
            if v9 == 0:
                v8.union_set(index(v3, v9, v10), v2 * v3)
            v4[v9][v10] = 1
            v12.append(max(0, v8.top() - v13 - 1))
        return v12[::-1]
