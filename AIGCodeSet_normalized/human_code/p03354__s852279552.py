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

    def size(self, a1):
        return -self.parents[self.find(a1)]

    def same(self, a1, a2):
        return self.find(a1) == self.find(a2)

    def members(self, a1):
        v1 = self.find(a1)
        return [i for v2 in range(self.n) if self.find(v2) == v1]

    def roots(self):
        return [i for v1, v2 in enumerate(self.parents) if v2 < 0]

    def group_count(self):
        return len(self.roots())

    def __str__(self):
        return '\n'.join(('{}: {}'.format(r, self.members(r)) for v1 in self.roots()))
v1, v2 = map(int, input().split())
v3 = C1(v1)
v4 = list(map(int, input().split()))
v5 = 0
for v6 in range(v2):
    v7, v8 = list(map(int, input().split()))
    v3.union(v7 - 1, v8 - 1)
for v6 in range(v1):
    if v3.same(v4[v6] - 1, v6):
        v5 += 1
print(v5)
