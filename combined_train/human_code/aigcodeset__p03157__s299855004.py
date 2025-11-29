import sys
input = sys.stdin.readline
v1, v2 = (int(i) for v3 in input().split())
v4 = [input() for v3 in range(v1)]

class C1:

    def __init__(self, a1):
        self.par = [v3 for v3 in range(a1)]
        self.size = [1] * a1
        self.N = a1

    def root(self, a1):
        if self.par[a1] == a1:
            return a1
        else:
            self.par[a1] = self.root(self.par[a1])
            return self.par[a1]

    def same(self, a1, a2):
        v1 = self.root(a1)
        v2 = self.root(a2)
        return v1 == v2

    def unite(self, a1, a2):
        v1 = self.root(a1)
        v2 = self.root(a2)
        if self.size[v1] < self.size[v2]:
            self.par[v1] = v2
            self.size[v2] += self.size[v1]
        else:
            self.par[v2] = v1
            self.size[v1] += self.size[v2]
v5 = C1(v1 * v2)
for v6 in range(v1):
    for v3 in range(v2):
        if v3 != v2 - 1 and v4[v6][v3 + 1] != v4[v6][v3]:
            v5.unite(v2 * v6 + v3, v2 * v6 + v3 + 1)
        if v6 != v1 - 1 and v4[v6 + 1][v3] != v4[v6][v3]:
            v5.unite(v2 * v6 + v3, v2 * (v6 + 1) + v3)
for v7 in range(v1 * v2):
    v5.root(v7)
v8 = [0] * (v1 * v2)
v9 = [0] * (v1 * v2)
for v6 in range(v1):
    for v3 in range(v2):
        v10 = v2 * v6 + v3
        if v4[v6][v3] == '.':
            v8[v5.par[v10]] += 1
        else:
            v9[v5.par[v10]] += 1
v11 = 0
for v3 in range(v1 * v2):
    v11 += v8[v3] * v9[v3]
print(v11)
