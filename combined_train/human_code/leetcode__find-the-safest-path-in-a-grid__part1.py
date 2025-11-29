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
        a1, a2 = (self.find_set(a1), self.find_set(a2))
        if a1 == a2:
            return False
        if self.rank[a1] > self.rank[a2]:
            a1, a2 = (a2, a1)
        self.set[a1] = self.set[a2]
        if self.rank[a1] == self.rank[a2]:
            self.rank[a2] += 1
        return True

class C2(object):

    def maximumSafenessFactor(self, a1):
        """
        """
        v1 = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def bfs():
            v1 = [[0 if a1[r][c] == 1 else -1 for v2 in range(len(a1[0]))] for v3 in range(len(a1))]
            v4 = [(v3, v2) for v3 in range(len(a1)) for v2 in range(len(a1[0])) if a1[v3][v2]]
            v5 = 0
            while v4:
                v6 = []
                for v3, v2 in v4:
                    for v7, v8 in v1:
                        v9, v10 = (v3 + v7, v2 + v8)
                        if not (0 <= v9 < len(v1) and 0 <= v10 < len(v1[0]) and (v1[v9][v10] == -1)):
                            continue
                        v1[v9][v10] = v5 + 1
                        v6.append((v9, v10))
                v4 = v6
                v5 += 1
            return v1
        v2 = bfs()
        v3 = [[] for v4 in range(len(a1) - 1 + (len(a1[0]) - 1) + 1)]
        for v5 in range(len(a1)):
            for v6 in range(len(a1[0])):
                v3[v2[v5][v6]].append((v5, v6))
        v7 = [[False] * len(a1[0]) for v4 in range(len(a1))]
        v8 = C1(len(a1) * len(a1[0]))
        for v9 in reversed(range(len(v3))):
            for v5, v6 in v3[v9]:
                for v10, v11 in v1:
                    v12, v13 = (v5 + v10, v6 + v11)
                    if not (0 <= v12 < len(v2) and 0 <= v13 < len(v2[0]) and (v7[v12][v13] == True)):
                        continue
                    v8.union_set(v12 * len(a1[0]) + v13, v5 * len(a1[0]) + v6)
                v7[v5][v6] = True
            if v8.find_set(0 * len(a1[0]) + 0) == v8.find_set((len(a1) - 1) * len(a1[0]) + (len(a1[0]) - 1)):
                break
        return v9
