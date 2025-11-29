class C1:

    def numOfUnplacedFruits(self, a1, a2):

        class SegTree:

            def __init__(self, a1):
                self.size = len(a1)
                self.tree = [0] * (4 * self.size)
                if self.size > 0:
                    self._construct(1, 0, self.size - 1, a1)

            def _construct(self, a1, a2, a3, a4):
                if a2 == a3:
                    self.tree[a1] = a4[a2]
                    return
                v1 = (a2 + a3) // 2
                self._construct(2 * a1, a2, v1, a4)
                self._construct(2 * a1 + 1, v1 + 1, a3, a4)
                self.tree[a1] = max(self.tree[2 * a1], self.tree[2 * a1 + 1])

            def _modify(self, a1, a2, a3, a4, a5):
                if a2 == a3:
                    self.tree[a1] = a5
                    return
                v1 = (a2 + a3) // 2
                if a4 <= v1:
                    self._modify(2 * a1, a2, v1, a4, a5)
                else:
                    self._modify(2 * a1 + 1, v1 + 1, a3, a4, a5)
                self.tree[a1] = max(self.tree[2 * a1], self.tree[2 * a1 + 1])

            def find_first_ge(self, a1, a2, a3, a4):
                if self.tree[a1] < a4:
                    return -1
                if a2 == a3:
                    return a2
                v1 = (a2 + a3) // 2
                v2 = self.find_first_ge(2 * a1, a2, v1, a4)
                if v2 != -1:
                    return v2
                return self.find_first_ge(2 * a1 + 1, v1 + 1, a3, a4)
        if not a2:
            return len(a1)
        v1 = SegTree(a2)
        v2 = 0
        for v3 in a1:
            v4 = v1.find_first_ge(1, 0, v1.size - 1, v3)
            if v4 == -1:
                v2 += 1
            else:
                v1._modify(1, 0, v1.size - 1, v4, 0)
        return v2
