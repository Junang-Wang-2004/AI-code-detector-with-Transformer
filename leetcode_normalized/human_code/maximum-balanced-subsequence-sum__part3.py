class C1(object):

    def maxBalancedSubsequenceSum(self, a1):
        """
        """
        v1 = float('-inf')

        class SegmentTree(object):

            def __init__(self, a1, a2=lambda _: None, a3=lambda x, y: max(x, y), a4=lambda x, y: max(x, y)):
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
                self.tree[v1] = self.update_fn(self.tree[v1], a2)
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
        v2 = {x: i for v3, v4 in enumerate(sorted({v4 - v3 for v3, v4 in enumerate(a1)}))}
        v5 = SegmentTree(len(v2))
        for v3, v4 in enumerate(a1):
            v6 = max(v5.query(0, v2[v4 - v3]), 0) + v4
            v5.update(v2[v4 - v3], v6)
        return v5.query(0, len(v2) - 1)
