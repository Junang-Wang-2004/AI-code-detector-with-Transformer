from bisect import bisect_left

class C1:

    def __init__(self, a1):
        self.size = a1
        self.tree = [0] * (a1 + 2)

    def update(self, a1, a2):
        while a1 <= self.size:
            self.tree[a1] += a2
            a1 += a1 & -a1

    def prefix_sum(self, a1):
        v1 = 0
        while a1 > 0:
            v1 += self.tree[a1]
            a1 -= a1 & -a1
        return v1

class C2:

    def minThreshold(self, a1, a2):
        v1 = a1[0]
        v2 = 0
        for v3 in a1[1:]:
            v2 = max(v2, v1 - v3)
            v1 = max(v1, v3)
        v4 = sorted(set(a1))
        v5 = {v: i + 1 for v6, v7 in enumerate(v4)}
        v8 = len(v4)

        def feasible(a1):
            v1 = C1(v8)
            v2 = 0
            for v3 in reversed(a1):
                v4 = v5[v3]
                v5 = v3 - a1
                v6 = bisect_left(v4, v5)
                v7 = v6 + 1
                v8 = v4 - 1
                if v7 <= v8:
                    v2 += v1.prefix_sum(v8) - v1.prefix_sum(v7 - 1)
                v1.update(v4, 1)
            return v2 >= a2
        v9 = 0
        v10 = v2
        while v9 <= v10:
            v11 = v9 + (v10 - v9) // 2
            if feasible(v11):
                v10 = v11 - 1
            else:
                v9 = v11 + 1
        v12 = v9
        return v12 if v12 <= v2 else -1
