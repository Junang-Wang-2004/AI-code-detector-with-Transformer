class C1:

    def __init__(self, a1):
        self.n = a1
        self.parents = [-1] * a1

    def find(self, a1):
        if self.parents[a1] < 0:
            return a1
        else:
            self.parents[a1] = self.find(self.parents[a1])
            return self.parents[a1]

    def union(self, a1, a2):
        a1 = self.find(a1)
        a2 = self.find(a2)
        if a1 == a2:
            return
        if self.parents[a1] > self.parents[a2]:
            a1, a2 = (a2, a1)
        self.parents[a1] += self.parents[a2]
        self.parents[a2] = a1

    def same(self, a1, a2):
        return self.find(a1) == self.find(a2)
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = C1(v1)
for v5 in range(v2):
    v6, v7 = map(int, input().split())
    v4.union(v6 - 1, v7 - 1)
v8 = 0
for v9 in range(v1):
    if v4.same(v9, v3[v9] - 1):
        v8 += 1
print(v8)
