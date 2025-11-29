class C1(object):

    def resultArray(self, a1, a2, a3):
        """
        """

        class SegmentTree(object):

            def __init__(self, a1, a2=lambda _: None, a3=lambda x, y: y if x is None else x if y is None else max(x, y), a4=lambda x: x):
                self.tree = [None] * (1 << (a1 - 1).bit_length() + 1)
                self.base = len(self.tree) >> 1
                self.query_fn = a3
                self.update_fn = a4
                for v1 in range(self.base, self.base + a1):
                    self.tree[v1] = a2(v1 - self.base)
                for v1 in reversed(range(1, self.base)):
                    self.tree[v1] = a3(self.tree[v1 << 1], self.tree[(v1 << 1) + 1])

            def update(self, a1, a2):
                v1 = self.base + a1
                self.tree[v1] = self.update_fn(a2)
                while v1 > 1:
                    v1 >>= 1
                    self.tree[v1] = self.query_fn(self.tree[v1 << 1], self.tree[(v1 << 1) + 1])

            def query(self, a1, a2):
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
                    a1 >>= 1
                    a2 >>= 1
                return self.query_fn(v3, v4)

        def build(a1):
            v1 = a1[a1] % a2
            v2 = [0] * (a2 + 1)
            v2[v1] = 1
            v2[-1] = v1
            return v2

        def update(a1):
            a1 %= a2
            v2 = [0] * (a2 + 1)
            v2[a1] = 1
            v2[-1] = a1
            return v2

        def query(a1, a2):
            if a1 is None:
                return a2
            if a2 is None:
                return a1
            v1 = a1[:]
            for v2 in range(a2):
                v1[a1[-1] * v2 % a2] += a2[v2]
            v1[-1] = a1[-1] * a2[-1] % a2
            return v1
        v1 = SegmentTree(len(a1), build_fn=build, update_fn=update, query_fn=query)
        v2 = [0] * len(a3)
        for v3, (v4, v5, v6, v7) in enumerate(a3):
            v1.update(v4, v5)
            v2[v3] = v1.query(v6, len(a1) - 1)[v7]
        return v2
