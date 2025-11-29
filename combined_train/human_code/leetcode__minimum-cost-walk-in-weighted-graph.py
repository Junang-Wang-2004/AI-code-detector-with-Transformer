class C1(object):

    def minimumCost(self, a1, a2, a3):
        """
        """

        class UnionFind(object):

            def __init__(self, a1):
                self.set = list(range(a1))
                self.rank = [0] * a1
                self.w = [-1] * a1

            def find_set(self, a1):
                v1 = []
                while self.set[a1] != a1:
                    v1.append(a1)
                    a1 = self.set[a1]
                while v1:
                    self.set[v1.pop()] = a1
                return a1

            def union_set(self, a1, a2, a3):
                a1, a2 = (self.find_set(a1), self.find_set(a2))
                if a1 == a2:
                    self.w[a1] &= a3
                    return False
                if self.rank[a1] > self.rank[a2]:
                    a1, a2 = (a2, a1)
                self.set[a1] = self.set[a2]
                if self.rank[a1] == self.rank[a2]:
                    self.rank[a2] += 1
                self.w[a2] &= self.w[a1] & a3
                return True

            def cost(self, a1):
                return self.w[self.find_set(a1)]
        v1 = UnionFind(a1)
        for v2, v3, v4 in a2:
            v1.union_set(v2, v3, v4)
        v5 = [-1] * len(a3)
        for v6, (v7, v8) in enumerate(a3):
            if v1.find_set(v7) != v1.find_set(v8):
                continue
            v5[v6] = v1.cost(v7) if v7 != v8 else 0
        return v5
