from sortedcontainers import SortedList

def f1(a1):
    v1 = []
    v2 = [-1] * (a1 + 1)
    for v3 in range(2, a1 + 1):
        if v2[v3] == -1:
            v2[v3] = v3
            v1.append(v3)
        for v4 in v1:
            if v3 * v4 > a1 or v4 > v2[v3]:
                break
            v2[v3 * v4] = v4
    return v2
v1 = 10 ** 5
v2 = f1(v1)

class C1(object):

    def maximumCount(self, a1, a2):
        """
        """

        class SegmentTree(object):

            def __init__(self, a1, a2=lambda x: 0, a3=lambda x, y: y if x is None else x if y is None else max(x, y), a4=lambda x, y: y if x is None else x + y):
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

            def __apply(self, a1, a2):
                self.tree[a1] = self.update_fn(self.tree[a1], a2)
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
                            self.tree[a1] = self.update_fn(self.tree[a1], self.lazy[a1])
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

        def add(a1, a2):
            v1 = a1[a1]
            if v2[v1] != v1:
                return
            if a2 == 1:
                lookup[v1].add(a1)
            if len(lookup[v1]) == 1:
                st.update(0, len(a1) - 2, a2)
            elif a1 == lookup[v1][0]:
                st.update(a1, lookup[v1][1] - 1, a2)
            elif a1 == lookup[v1][-1]:
                st.update(lookup[v1][-2], a1 - 1, a2)
            if a2 == -1:
                lookup[v1].remove(a1)
        v1 = collections.defaultdict(SortedList)
        v2 = SegmentTree(len(a1) - 1)
        for v3 in range(len(a1)):
            add(v3, +1)
        v4 = [0] * len(a2)
        for v3, (v5, v6) in enumerate(a2):
            if a1[v5] != v6:
                add(v5, -1)
                a1[v5] = v6
                add(v5, +1)
            v4[v3] = v2.tree[1]
        return v4
