class C1(object):

    def longestBalanced(self, a1):
        """
        """

        class SegmentTree(object):

            def __init__(self, a1):
                self.min = [0] * (1 << (a1 - 1).bit_length() + 1)
                self.max = [0] * (1 << (a1 - 1).bit_length() + 1)
                self.base = len(self.min) >> 1
                self.lazy = [0] * self.base

            def __apply(self, a1, a2):
                self.min[a1] += a2
                self.max[a1] += a2
                if a1 < self.base:
                    self.lazy[a1] += a2

            def __push(self, a1):
                for v1 in reversed(range(1, a1.bit_length())):
                    v2 = a1 >> v1
                    if self.lazy[v2]:
                        self.__apply(v2 << 1, self.lazy[v2])
                        self.__apply(v2 << 1 | 1, self.lazy[v2])
                        self.lazy[v2] = 0

            def update(self, a1, a2, a3):

                def pull(a1):
                    while a1 > 1:
                        a1 >>= 1
                        self.min[a1] = self.min[a1 << 1] if self.min[a1 << 1] < self.min[a1 << 1 | 1] else self.min[a1 << 1 | 1]
                        self.max[a1] = self.max[a1 << 1] if self.max[a1 << 1] > self.max[a1 << 1 | 1] else self.max[a1 << 1 | 1]
                        if self.lazy[a1]:
                            self.min[a1] += self.lazy[a1]
                            self.max[a1] += self.lazy[a1]
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

            def binary_search(self, a1):
                v1 = 1
                while not v1 >= self.base:
                    if self.lazy[v1]:
                        self.__apply(v1 << 1, self.lazy[v1])
                        self.__apply(v1 << 1 | 1, self.lazy[v1])
                        self.lazy[v1] = 0
                    v1 <<= 1
                    if not self.min[v1] <= a1 <= self.max[v1]:
                        v1 |= 1
                return v1 - self.base
        v1 = len(a1) + 1
        v2 = SegmentTree(v1)
        v3 = v4 = 0
        v5 = {}
        for v6, v7 in enumerate(a1, 1):
            v8 = +1 if v7 & 1 else -1
            if v7 in v5:
                v2.update(v5[v7], v1 - 1, -v8)
                v4 -= v8
            v4 += v8
            v5[v7] = v6
            v2.update(v5[v7], v1 - 1, +v8)
            v9 = v6 - v2.binary_search(v4)
            if v9 > v3:
                v3 = v9
        return v3
