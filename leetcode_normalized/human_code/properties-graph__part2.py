class C1(object):

    def numberOfComponents(self, a1, a2):
        """
        """

        class UnionFind(object):

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
        v1 = [set(p) for v2 in a1]
        v3 = UnionFind(len(a1))
        return len(a1) - sum((sum((x in v1[j] for v4 in v1[i])) >= a2 and v3.union_set(i, j) for v5 in range(len(v1)) for v6 in range(v5 + 1, len(v1))))
