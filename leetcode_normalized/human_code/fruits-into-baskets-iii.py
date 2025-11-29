class C1(object):

    def numOfUnplacedFruits(self, a1, a2):
        """
        """

        class SegmentTree(object):

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

            def binary_search(self, a1):
                if self.tree[1] < a1:
                    return -1
                v1 = 1
                while not v1 >= self.base:
                    if self.tree[2 * v1] >= a1:
                        v1 = 2 * v1
                    else:
                        v1 = 2 * v1 + 1
                return v1 - self.base

        def build(a1):
            return a2[a1]
        v1 = SegmentTree(len(a2), build_fn=build)
        v2 = 0
        for v3 in a1:
            v4 = v1.binary_search(v3)
            if v4 == -1:
                v2 += 1
            else:
                v1.update(v4, 0)
        return v2
