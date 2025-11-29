class C1:

    def __init__(self, a1):
        self.v = [-1 for v1 in range(a1)]

    def find(self, a1):
        if self.v[a1] < 0:
            return a1
        else:
            self.v[a1] = self.find(self.v[a1])
            return self.v[a1]

    def unite(self, a1, a2):
        a1 = self.find(a1)
        a2 = self.find(a2)
        if a1 == a2:
            return
        if -self.v[a1] < -self.v[a2]:
            a1, a2 = (a2, a1)
        self.v[a1] += self.v[a2]
        self.v[a2] = a1

    def root(self, a1):
        return self.v[a1] < 0

    def same(self, a1, a2):
        return self.find(a1) == self.find(a2)

    def size(self, a1):
        return -self.v[self.find(a1)]
v1 = [0, 0, 1, -1]
v2 = [1, -1, 0, 0]
v3, v4 = map(int, input().split())
v5 = [input() for v6 in range(v3)]
v7 = C1(2 * v3 * v4)
for v8 in range(v3):
    for v9 in range(v4):
        if v5[v8][v9] == '#':
            for v10 in range(4):
                v11 = v8 + v1[v10]
                v12 = v9 + v2[v10]
                if 0 <= v11 < v3 and 0 <= v12 < v4:
                    if v5[v11][v12] == '.':
                        v7.unite(v8 * v4 + v9, (v11 * v4 + v12) * 2)
        else:
            for v10 in range(4):
                v11 = v8 + v1[v10]
                v12 = v9 + v2[v10]
                if 0 <= v11 < v3 and 0 <= v12 < v4:
                    if v5[v11][v12] == '#':
                        v7.unite((v8 * v4 + v9) * 2, v11 * v4 + v12)
v13 = 0
for v8 in range(v3):
    for v9 in range(v4):
        if v7.root(v8 * v4 + v9):
            v14 = v7.size(v8 * v4 + v9)
            v15 = v14 // 2
            v16 = v14 - v15
            v13 += v15 * v16
        elif v7.root((v8 * v4 + v9) * 2):
            v14 = v7.size((v8 * v4 + v9) * 2)
            v16 = v14 // 2
            v15 = v14 - v16
            v13 += v15 * v16
print(v13)
