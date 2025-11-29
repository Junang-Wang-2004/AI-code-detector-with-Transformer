class C1(object):

    def handleQuery(self, a1, a2, a3):
        """
        """

        class SegmentTree(object):

            def __init__(self, a1, a2=lambda _: 0, a3=lambda x, y: y if x is None else max(x, y), a4=lambda x, y: y if x is None else x + y):
                self.base = a1
                self.H = (a1 - 1).bit_length()
                self.query_fn = a3
                self.update_fn = a4
                self.tree = [None] * (2 * a1)
                self.lazy = [None] * a1
                for v1 in range(self.base, self.base + a1):
                    self.tree[v1] = a2(v1 - self.base)
                for v1 in reversed(range(1, self.base)):
                    self.tree[v1] = a3(self.tree[2 * v1], self.tree[2 * v1 + 1])

            def __apply(self, a1, a2):
                self.tree[a1] = self.update_fn(self.tree[a1], a2)
                if a1 < self.base:
                    self.lazy[a1] = self.update_fn(self.lazy[a1], a2)

            def update(self, a1, a2, a3):

                def pull(a1):
                    while a1 > 1:
                        a1 >>= 1
                        self.tree[a1] = self.query_fn(self.tree[a1 << 1], self.tree[(a1 << 1) + 1])
                        if self.lazy[a1] is not None:
                            self.tree[a1] = self.update_fn(self.tree[a1], self.lazy[a1])
                if a1 > a2:
                    return
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

                def push(a1):
                    v1 = self.H
                    while v1:
                        v2 = a1 >> v1
                        if self.lazy[v2] is not None:
                            self.__apply(v2 << 1, self.lazy[v2])
                            self.__apply((v2 << 1) + 1, self.lazy[v2])
                            self.lazy[v2] = None
                        v1 -= 1
                v1 = None
                if a1 > a2:
                    return v1
                a1 += self.base
                a2 += self.base
                push(a1)
                push(a2)
                while a1 <= a2:
                    if a1 & 1:
                        v1 = self.query_fn(v1, self.tree[a1])
                        a1 += 1
                    if a2 & 1 == 0:
                        v1 = self.query_fn(v1, self.tree[a2])
                        a2 -= 1
                    a1 >>= 1
                    a2 >>= 1
                return v1
        v1 = SegmentTree(len(a1), build_fn=lambda i: (a1[i], a1[i] ^ 1), query_fn=lambda x, y: y if x is None else (x[0] + y[0], x[1] + y[1]), update_fn=lambda x, y: y if x is None else (x[1], x[0]) if y == (1, 0) else x)
        v2 = []
        v3 = sum(a2)
        for v4, v5, v6 in a3:
            if v4 == 1:
                v1.update(v5, v6, (1, 0))
            elif v4 == 2:
                v3 += v1.query(0, len(a1) - 1)[0] * v5
            elif v4 == 3:
                v2.append(v3)
        return v2
