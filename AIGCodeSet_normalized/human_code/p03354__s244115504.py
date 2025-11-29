import sys
input = sys.stdin.readline
v1, v2 = map(int, input().split())
v3 = list(map(lambda x: int(x) - 1, input().split()))

class C1:

    def __init__(self, a1):
        self.parent = list(range(a1))

    def get_root(self, a1):
        v1 = self.parent[a1]
        if v1 == a1:
            return v1
        else:
            v1 = self.get_root(v1)
            self.parent[a1] = v1
            return v1

    def are_in_same_union(self, a1, a2):
        v1 = self.get_root(a1)
        v2 = self.get_root(a2)
        if v1 == v2:
            return True
        else:
            return False

    def unite(self, a1, a2):
        v1 = self.get_root(a1)
        v2 = self.get_root(a2)
        if v1 == v2:
            return
        self.parent[v2] = v1
v4 = C1(v1)
for v5 in range(v2):
    v6, v7 = map(int, input().split())
    v6 -= 1
    v7 -= 1
    v4.unite(v6, v7)
v8 = 0
for v9 in range(v1):
    v10 = v3[v9]
    if v10 == v9:
        v8 += 1
    elif v4.are_in_same_union(v9, v10):
        v8 += 1
print(v8)
