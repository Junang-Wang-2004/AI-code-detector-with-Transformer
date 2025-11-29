from sortedcontainers import SortedList

class C1(object):

    def getResults(self, a1):
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

        def update(a1):
            sl.add(a1)
            v1 = sl.bisect_left(a1)
            st.update(val_to_idx[a1], a1 - (sl[v1 - 1] if v1 - 1 >= 0 else 0))
            if v1 + 1 < len(sl):
                st.update(val_to_idx[sl[v1 + 1]], sl[v1 + 1] - a1)
        v1 = {x: i for v2, v3 in enumerate(sorted((q[1] for v4 in a1 if v4[0] == 1)))}
        v5 = SegmentTree(len(v1))
        v6 = SortedList()
        v7 = []
        for v4 in a1:
            if v4[0] == 1:
                update(v4[1])
            else:
                v2 = v6.bisect_left(v4[1])
                v7.append(v4[1] - (v6[v2 - 1] if v2 - 1 >= 0 else 0) >= v4[2] or (v2 - 1 >= 0 and v5.query(0, v1[v6[v2 - 1]]) >= v4[2]))
        return v7
