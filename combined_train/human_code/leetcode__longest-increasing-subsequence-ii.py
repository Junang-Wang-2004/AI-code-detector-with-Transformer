import bisect

class C1(object):

    def __init__(self, a1, a2=lambda _: 0, a3=lambda x, y: y if x is None else x if y is None else max(x, y), a4=lambda x: x):
        self.tree = [None] * (2 * 2 ** (a1 - 1).bit_length())
        self.base = len(self.tree) // 2
        self.query_fn = a3
        self.update_fn = a4
        for v1 in range(self.base, self.base + a1):
            self.tree[v1] = a2(v1 - self.base)
        for v1 in reversed(range(1, self.base)):
            self.tree[v1] = a3(self.tree[2 * v1], self.tree[2 * v1 + 1])

    def update(self, a1, a2):
        v1 = self.base + a1
        self.tree[v1] = self.update_fn(a2)
        while v1 > 1:
            v1 //= 2
            self.tree[v1] = self.query_fn(self.tree[v1 * 2], self.tree[v1 * 2 + 1])

    def query(self, a1, a2):
        if a1 > a2:
            return 0
        a1 += self.base
        a2 += self.base
        v3 = v4 = None
        while a1 <= a2:
            if a1 & 1:
                v3 = self.query_fn(v3, self.tree[a1])
                a1 += 1
            if a2 & 1 == 0:
                v4 = self.query_fn(self.tree[a2], v4)
                a2 -= 1
            a1 //= 2
            a2 //= 2
        return self.query_fn(v3, v4)

class C2(object):

    def lengthOfLIS(self, a1, a2):
        """
        """
        v1 = sorted({x - 1 for v2 in a1})
        v3 = {v2: i for v4, v2 in enumerate(v1)}
        v5 = C1(len(v3))
        for v2 in a1:
            v2 -= 1
            v5.update(v3[v2], v5.query(bisect.bisect_left(v1, v2 - a2), v3[v2] - 1) + 1)
        return v5.tree[1]
