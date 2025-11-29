import bisect

class C1:

    def __init__(self, a1):
        self.size = a1
        self.tree = [0] * (a1 + 1)

    def add(self, a1, a2):
        while a1 <= self.size:
            self.tree[a1] += a2
            a1 += a1 & -a1

    def get_sum(self, a1):
        v1 = 0
        while a1 > 0:
            v1 += self.tree[a1]
            a1 -= a1 & -a1
        return v1

def f3(a1, a2):
    a2.sort()
    v1 = C1(a1)
    v2 = 0
    for v3 in range(a1):
        v4 = bisect.bisect_left(a2, a2[v3] + 1)
        v5 = v1.get_sum(v4 - 1)
        v6 = v3 - v4 + 1
        v2 += min(v5, v6)
        v1.add(v4, a2[v3])
    return v2
v1 = int(input())
v2 = list(map(int, input().split()))
print(f3(v1, v2))
