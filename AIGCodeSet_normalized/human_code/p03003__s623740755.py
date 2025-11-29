from collections import defaultdict

class C1:

    def __init__(self, a1):
        self.size = a1
        self.tree = [0] * (a1 + 1)

    def sum(self, a1):
        v1 = 0
        while a1 > 0:
            v1 = (v1 + self.tree[a1]) % 1000000007
            a1 -= a1 & -a1
        return v1

    def add(self, a1, a2):
        while a1 <= self.size:
            self.tree[a1] = (self.tree[a1] + a2) % 1000000007
            a1 += a1 & -a1
v1, v2 = list(map(int, input().split()))
v3 = list(map(int, input().split()))
v4 = list(map(int, input().split()))
v5 = defaultdict(list)
for v6, v7 in reversed(list(enumerate(v3))):
    v5[v7].append(v6)
v8 = C1(v1 + 1)
v8.add(1, 1)
for v9 in v4:
    if v9 not in v5:
        continue
    for v6 in v5[v9]:
        v8.add(v6 + 2, v8.sum(v6 + 1))
print(v8.sum(v1 + 1))
