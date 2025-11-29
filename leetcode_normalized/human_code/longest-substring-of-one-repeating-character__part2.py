import itertools

class C1(object):

    def __init__(self, a1, a2=lambda _: float('inf'), a3=lambda x, y: y if x is None else x if y is None else min(x, y), a4=lambda x: x):
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
            return None
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

    def longestRepeating(self, a1, a2, a3):
        """
        """
        v1, v2, v3, v4, v5, v6, v7 = range(7)

        def build(a1):
            return update(a1[a1])

        def update(a1):
            v1 = [0] * v7
            v1[v5] = v1[v3] = v1[v4] = v1[v6] = 1
            v1[v1] = v1[v2] = a1
            return v1

        def query(a1, a2):
            return a2 if a1 is None else a1 if a2 is None else [a1[v1], a2[v2], a1[v3] + (a2[v3] if a1[v3] == a1[v5] and a1[v2] == a2[v1] else 0), a2[v4] + (a1[v4] if a2[v4] == a2[v5] and a2[v1] == a1[v2] else 0), a1[v5] + a2[v5], max(a1[v6], a2[v6], a1[v4] + a2[v3] if a1[v2] == a2[v1] else 0)]
        v8 = []
        v9 = C1(len(a1), build_fn=build, query_fn=query, update_fn=update)
        for v10, v11 in zip(a2, a3):
            v9.update(v11, v10)
            v8.append(v9.query(0, len(a1) - 1)[v6])
        return v8
