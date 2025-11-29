class C1(object):

    def leftmostBuildingQueries(self, a1, a2):
        """
        """

        class SegmentTree(object):

            def __init__(self, a1, a2=lambda _: None, a3=lambda x, y: max(x, y)):
                self.tree = [None] * (2 * 2 ** (a1 - 1).bit_length())
                self.build_fn = a2
                self.query_fn = a3
                self.build(0, a1 - 1, 1)

            def build(self, a1, a2, a3):
                if a1 == a2:
                    self.tree[a3] = self.build_fn(a1)
                    return
                v1 = a1 + (a2 - a1) // 2
                self.build(a1, v1, a3 * 2)
                self.build(v1 + 1, a2, a3 * 2 + 1)
                self.tree[a3] = self.query_fn(self.tree[a3 * 2], self.tree[a3 * 2 + 1])

            def binary_search(self, a1, a2, a3, a4, a5, a6):
                if a4 < a1 or a3 > a2:
                    return -1
                if a1 <= a3 and a4 <= a2:
                    if not self.tree[a5] > a6:
                        return -1
                    if a3 == a4:
                        return a3
                v1 = a3 + (a4 - a3) // 2
                v2 = self.binary_search(a1, a2, a3, v1, a5 * 2, a6)
                return v2 if v2 != -1 else self.binary_search(a1, a2, v1 + 1, a4, a5 * 2 + 1, a6)

        def build(a1):
            return a1[a1]
        v1 = [-1] * len(a2)
        v2 = SegmentTree(len(a1), build_fn=build)
        for v3, (v4, v5) in enumerate(a2):
            if v4 > v5:
                v4, v5 = (v5, v4)
            if v4 == v5 or a1[v4] < a1[v5]:
                v1[v3] = v5
                continue
            v1[v3] = v2.binary_search(v5 + 1, len(a1) - 1, 0, len(a1) - 1, 1, a1[v4])
        return v1
