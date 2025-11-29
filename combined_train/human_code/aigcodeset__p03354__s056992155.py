class C1:

    def __init__(self, a1):
        self.n = a1
        self.root = [-1] * (a1 + 1)
        self.rank = [0] * (a1 + 1)

    def FindRoot(self, a1):
        if self.root[a1] < 0:
            return a1
        else:
            self.root[a1] = self.FindRoot(self.root[a1])
            return self.root[a1]

    def Unite(self, a1, a2):
        a1 = self.FindRoot(a1)
        a2 = self.FindRoot(a2)
        if a1 == a2:
            return
        elif self.rank[a1] > self.rank[a2]:
            self.root[a1] += self.root[a2]
            self.root[a2] = a1
        elif self.rank[a1] <= self.rank[a2]:
            self.root[a2] += self.root[a1]
            self.root[a1] = a2
            if self.rank[a1] == self.rank[a2]:
                self.rank[a2] += 1

    def isSameGroup(self, a1, a2):
        return self.FindRoot(a1) == self.FindRoot(a2)

    def Count(self, a1):
        return -self.root[self.FindRoot(a1)]
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = C1(v1 + 1)
for v5 in range(v2):
    v6, v7 = map(int, input().split())
    v4.Unite(v6, v7)
v8 = 0
for v9 in range(v1):
    if v3[v9] == v9 + 1:
        v8 += 1
    elif v4.isSameGroup(v9 + 1, v3[v9]):
        v8 += 1
print(v8)
