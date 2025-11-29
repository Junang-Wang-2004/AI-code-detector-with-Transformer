class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.size = [1] * a1
        self.snapshots = []
        self.undos = []

    def find_set(self, a1):
        v1 = []
        while self.set[a1] != a1:
            v1.append(a1)
            a1 = self.set[a1]
        while v1:
            v3 = v1.pop()
            self.undos.append((~v3, self.set[v3]))
            self.set[v3] = a1
        return a1

    def union_set(self, a1, a2):
        a1, a2 = (self.find_set(a1), self.find_set(a2))
        if a1 == a2:
            return False
        if self.size[a1] > self.size[a2]:
            a1, a2 = (a2, a1)
        self.undos.append((a1, a2))
        self.set[a1] = self.set[a2]
        self.size[a2] += self.size[a1]
        return True

    def total(self, a1):
        return self.size[self.find_set(a1)]

    def snapshot(self):
        self.snapshots.append(len(self.undos))

    def rollback(self):
        for v1 in range(len(self.undos) - self.snapshots.pop()):
            v2, v3 = self.undos.pop()
            if v2 >= 0:
                self.size[v3] -= self.size[v2]
                self.set[v2] = v2
            else:
                self.set[~v2] = v3

class C2(object):

    def minDays(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def floodfill(a1, a2, a3, a4):
            v1 = [(a2, a3)]
            a4[a2][a3] = 1
            while v1:
                a2, a3 = v1.pop()
                for v4, v5 in v1:
                    v6, v7 = (a2 + v4, a3 + v5)
                    if not (0 <= v6 < R and 0 <= v7 < C and a1[v6][v7] and (not a4[v6][v7])):
                        continue
                    a4[v6][v7] = 1
                    v1.append((v6, v7))

        def count_islands(a1):
            v1 = [[0] * C for v2 in range(R)]
            v3 = 0
            for v4 in range(R):
                for v5 in range(C):
                    if a1[v4][v5] == 0 or v1[v4][v5]:
                        continue
                    v3 += 1
                    floodfill(a1, v4, v5, v1)
            return v3

        def merge(a1):
            v1, v2 = divmod(a1, C)
            for v3, v4 in v1:
                v5, v6 = (v1 + v3, v2 + v4)
                v7 = v5 * C + v6
                if 0 <= v5 < R and 0 <= v6 < C and (a1[v5][v6] == a1[v1][v2]) and lookup[v7]:
                    uf.union_set(a1, v7)

        def check(a1):
            v1, v2 = divmod(a1, C)
            if a1[v1][v2] == 0:
                return False
            v3 = set()
            for v4, v5 in v1:
                v6, v7 = (v1 + v4, v2 + v5)
                if 0 <= v6 < R and 0 <= v7 < C and (a1[v6][v7] == a1[v1][v2]):
                    v3.add(uf.find_set(v6 * C + v7))
            return len(v3) != 1

        def dfs(a1, a2):
            if a1 == a2:
                return check(a1)
            v1 = a1 + (a2 - a1) // 2
            v2, v3, v4, v5 = (a1, v1, v1 + 1, a2)
            for v6 in range(2):
                uf.snapshot()
                for v7 in range(v2, v3 + 1):
                    lookup[v7] = True
                    merge(v7)
                if dfs(v4, v5):
                    return True
                for v7 in range(v2, v3 + 1):
                    lookup[v7] = False
                uf.rollback()
                v2, v3, v4, v5 = (v4, v5, v2, v3)
            return False
        v2, v3 = (len(a1), len(a1[0]))
        if count_islands(a1) != 1:
            return 0
        v4 = C1(v2 * v3)
        v5 = [False] * (v2 * v3)
        return 1 if dfs(0, v2 * v3 - 1) else 2
