import heapq

class C1(object):

    def maxTotalValue(self, a1, a2):
        """
        """

        class SegmentTree(object):

            def __init__(self, a1, a2, a3):
                self.tree = [None] * (1 << (a1 - 1).bit_length() + 1)
                self.base = len(self.tree) >> 1
                self.query_fn = a3
                for v1 in range(self.base, self.base + a1):
                    self.tree[v1] = a2(v1 - self.base)
                for v1 in reversed(range(1, self.base)):
                    self.tree[v1] = a3(self.tree[v1 << 1], self.tree[(v1 << 1) + 1])

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
                    a1 >>= 1
                    a2 >>= 1
                return self.query_fn(v3, v4)
        v1 = SegmentTree(len(a1), build_fn=lambda x: a1[x], query_fn=lambda x, y: y if x is None else x if y is None else min(x, y))
        v2 = SegmentTree(len(a1), build_fn=lambda x: a1[x], query_fn=lambda x, y: y if x is None else x if y is None else max(x, y))
        v3 = [(-(v2.query(i, len(a1) - 1) - v1.query(i, len(a1) - 1)), (i, len(a1) - 1)) for v4 in range(len(a1))]
        heapq.heapify(v3)
        v5 = 0
        for v6 in range(a2):
            v7, (v4, v8) = heappop(v3)
            v5 += -v7
            if v4 <= v8 - 1:
                heapq.heappush(v3, (-(v2.query(v4, v8 - 1) - v1.query(v4, v8 - 1)), (v4, v8 - 1)))
        return v5
