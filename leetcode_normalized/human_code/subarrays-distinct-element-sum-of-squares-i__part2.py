class C1(object):

    def sumCounts(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        class SegmentTree(object):

            def __init__(self, a1, a2=None, a3=lambda x, y: y if x is None else x if y is None else (x + y) % v1, a4=lambda x, y: y if x is None else (x + y) % v1):
                self.tree = [None] * (1 << (a1 - 1).bit_length() + 1)
                self.base = len(self.tree) >> 1
                self.lazy = [None] * self.base
                self.query_fn = a3
                self.update_fn = a4
                if a2 is not None:
                    for v1 in range(self.base, self.base + a1):
                        self.tree[v1] = a2(v1 - self.base)
                    for v1 in reversed(range(1, self.base)):
                        self.tree[v1] = a3(self.tree[v1 << 1], self.tree[(v1 << 1) + 1])
                self.count = [1] * len(self.tree)
                for v1 in reversed(range(1, self.base)):
                    self.count[v1] = self.count[v1 << 1] + self.count[(v1 << 1) + 1]

            def __apply(self, a1, a2):
                self.tree[a1] = self.update_fn(self.tree[a1], a2 * self.count[a1])
                if a1 < self.base:
                    self.lazy[a1] = self.update_fn(self.lazy[a1], a2)

            def __push(self, a1):
                for v1 in reversed(range(1, a1.bit_length())):
                    v2 = a1 >> v1
                    if self.lazy[v2] is not None:
                        self.__apply(v2 << 1, self.lazy[v2])
                        self.__apply((v2 << 1) + 1, self.lazy[v2])
                        self.lazy[v2] = None

            def update(self, a1, a2, a3):

                def pull(a1):
                    while a1 > 1:
                        a1 >>= 1
                        self.tree[a1] = self.query_fn(self.tree[a1 << 1], self.tree[(a1 << 1) + 1])
                        if self.lazy[a1] is not None:
                            self.tree[a1] = self.update_fn(self.tree[a1], self.lazy[a1] * self.count[a1])
                a1 += self.base
                a2 += self.base
                v3, v4 = (a1, a2)
                while a1 <= a2:
                    if a1 & 1:
                        self.__apply(a1, a3)
                        a1 += 1
                    if a2 & 1 == 0:
                        self.__apply(a2, a3)
                        a2 -= 1
                    a1 >>= 1
                    a2 >>= 1
                pull(v3)
                pull(v4)

            def query(self, a1, a2):
                if a1 > a2:
                    return None
                a1 += self.base
                a2 += self.base
                self.__push(a1)
                self.__push(a2)
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
        v2 = v3 = 0
        v4 = {}
        v5 = SegmentTree(len(a1))
        for v6 in range(len(a1)):
            v7 = v4[a1[v6]] if a1[v6] in v4 else -1
            v3 = (v3 + (v6 - v7 + 2 * max(v5.query(v7 + 1, v6), 0))) % v1
            v2 = (v2 + v3) % v1
            v5.update(v7 + 1, v6, 1)
            v4[a1[v6]] = v6
        return v2
