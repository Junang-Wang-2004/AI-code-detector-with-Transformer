class C1(object):

    def maximumSumSubsequence(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3, v4, v5 = list(range(4))

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
            return [max(a1[a1], 0), 0, 0, 0]

        def query(a1, a2):
            if a1 is None:
                return a2
            if a2 is None:
                return a1
            return [max(a1[v4] + a2[v3], a1[v2] + a2[v3], a1[v4] + a2[v2]), max(a1[v5] + a2[v3], a1[v3] + a2[v3], a1[v5] + a2[v2]), max(a1[v4] + a2[v5], a1[v2] + a2[v5], a1[v4] + a2[v4]), max(a1[v5] + a2[v5], a1[v3] + a2[v5], a1[v5] + a2[v4])]
        v6 = SegmentTree(len(a1), build_fn=build, query_fn=query)
        v7 = 0
        for v8, v9 in a2:
            v6.update(v8, [max(v9, 0), 0, 0, 0])
            v7 = (v7 + max(v6.tree[1])) % v1
        return v7
