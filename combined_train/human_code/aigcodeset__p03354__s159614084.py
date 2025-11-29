def f1(a1, a2, a3, a4):

    class UnionFind(object):

        def __init__(self, a1):
            self.p = list(range(a1))
            self.rank = [0] * a1
            self.size = [1] * a1

        def find(self, a1):
            if self.p[a1] != a1:
                self.p[a1] = self.find(self.p[a1])
            return self.p[a1]

        def is_same(self, a1, a2):
            return self.find(a1) == self.find(a2)

        def union(self, a1, a2):
            v1 = self.find(a1)
            v2 = self.find(a2)
            if v1 == v2:
                return
            if self.rank[v1] < self.rank[v2]:
                self.p[v1] = v2
                self.size[v2] += self.size[v1]
                self.size[v1] = 0
            else:
                self.p[v2] = v1
                self.size[v1] += self.size[v2]
                self.size[v2] = 0
                if self.rank[v1] == self.rank[v2]:
                    self.rank[v1] += 1

        def get_size(self, a1):
            return self.size[self.find(a1)]

        def show(self):
            return self.p
    v1 = 0
    v2 = UnionFind(a1)
    for v3, v4 in a4:
        v2.union(v3 - 1, v4 - 1)
    for v5 in range(a1):
        if v2.is_same(a3[v5] - 1, v5):
            v1 += 1
    return v1
v1, v2 = [int(i) for v3 in input().split()]
v4 = [int(v3) for v3 in input().split()]
v5 = [[int(v3) for v3 in input().split()] for v6 in range(v2)]
print(f1(v1, v2, v4, v5))
