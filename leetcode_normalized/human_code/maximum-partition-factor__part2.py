class C1(object):

    def maxPartitionFactor(self, a1):
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
                    v3 = v1.pop()
                    self.set[v3] = a1
                return a1

            def union_set(self, a1, a2):
                a1, a2 = (self.find_set(a1), self.find_set(a2))
                if a1 == a2:
                    return False
                if self.rank[a1] > self.rank[a2]:
                    a1, a2 = (a2, a1)
                if self.rank[a1] == self.rank[a2]:
                    self.rank[a2] += 1
                self.set[a1] = self.set[a2]
                return True

        def dist(a1, a2):
            return abs(a1[a1][0] - a1[a2][0]) + abs(a1[a1][1] - a1[a2][1])
        v1 = sorted(((dist(u, v), u, v) for v2 in range(len(a1)) for v3 in range(v2 + 1, len(a1))))
        v4 = UnionFind(len(a1))
        v5 = [-1] * len(a1)
        for v6, v2, v3 in v1:
            if v4.find_set(v2) == v4.find_set(v3):
                return v6
            if v5[v2] != -1:
                v4.union_set(v5[v2], v3)
            else:
                v5[v2] = v3
            if v5[v3] != -1:
                v4.union_set(v5[v3], v2)
            else:
                v5[v3] = v2
        return 0
