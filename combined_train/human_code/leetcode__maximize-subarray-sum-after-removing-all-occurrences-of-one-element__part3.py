import collections

class C1(object):

    def maxSubarraySum(self, a1):
        """
        """
        v1, v2, v3, v4 = list(range(4))

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
            return [a1[a1]] * 4

        def query(a1, a2):
            if a1 is None:
                return a2
            if a2 is None:
                return a1
            return [max(a1[v1], a2[v1], a1[v4] + a2[v3]), a1[v2] + a2[v2], max(a1[v3], a1[v2] + a2[v3]), max(a2[v4], a1[v4] + a2[v2])]
        v5 = max(a1)
        if v5 < 0:
            return v5
        v6 = min(a1)
        if v6 >= 0:
            return sum(a1)
        v7 = collections.defaultdict(list)
        for v8, v9 in enumerate(a1):
            v7[v9].append(v8)
        v10 = SegmentTree(len(a1), build_fn=build, query_fn=query)
        v11 = v10.tree[1][0]
        for v12, v13 in v7.items():
            for v8 in v13:
                v10.update(v8, None)
            v11 = max(v11, v10.tree[1][0])
            for v8 in v13:
                v10.update(v8, [v12] * 4)
        return v11
