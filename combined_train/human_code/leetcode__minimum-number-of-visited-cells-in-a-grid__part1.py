class C1(object):

    def __init__(self, a1):
        self.set = list(range(a1))
        self.rank = [0] * a1
        self.right = list(range(a1))

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
        self.right[a2] = max(self.right[a1], self.right[a2])
        return True

    def right_set(self, a1):
        return self.right[self.find_set(a1)]

class C2(object):

    def minimumVisitedCells(self, a1):
        """
        """
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [C1(v2 + 1) for v4 in range(v1)]
        v5 = [C1(v1 + 1) for v4 in range(v2)]
        v6, v7, v8 = (1, 0, 0)
        v9 = [(v7, v8)]
        v3[v7].union_set(v8, v8 + 1)
        v5[v8].union_set(v7, v7 + 1)
        while v9:
            v10 = []
            for v7, v8 in v9:
                if (v7, v8) == (v1 - 1, v2 - 1):
                    return v6
                while v3[v7].right_set(v8) <= min(v8 + a1[v7][v8], v2 - 1):
                    v11 = v3[v7].right_set(v8)
                    v10.append((v7, v11))
                    v5[v11].union_set(v7, v7 + 1)
                    v3[v7].union_set(v11, v11 + 1)
                while v5[v8].right_set(v7) <= min(v7 + a1[v7][v8], v1 - 1):
                    v11 = v5[v8].right_set(v7)
                    v10.append((v11, v8))
                    v3[v11].union_set(v8, v8 + 1)
                    v5[v8].union_set(v11, v11 + 1)
            v9 = v10
            v6 += 1
        return -1
