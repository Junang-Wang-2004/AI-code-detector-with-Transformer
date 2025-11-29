class C1:

    def __init__(self, a1):
        self.length = len(a1)
        self.segment = [0] * (4 * self.length)
        if self.length > 0:
            self._build_tree(1, 0, self.length - 1, a1)

    def _build_tree(self, a1, a2, a3, a4):
        if a2 == a3:
            self.segment[a1] = a4[a2]
            return
        v1 = (a2 + a3) // 2
        self._build_tree(2 * a1, a2, v1, a4)
        self._build_tree(2 * a1 + 1, v1 + 1, a3, a4)
        self.segment[a1] = self.segment[2 * a1] + self.segment[2 * a1 + 1]

    def update(self, a1, a2):
        self._modify_tree(1, 0, self.length - 1, a1, a2)

    def _modify_tree(self, a1, a2, a3, a4, a5):
        if a2 == a3:
            self.segment[a1] = a5
            return
        v1 = (a2 + a3) // 2
        if a4 <= v1:
            self._modify_tree(2 * a1, a2, v1, a4, a5)
        else:
            self._modify_tree(2 * a1 + 1, v1 + 1, a3, a4, a5)
        self.segment[a1] = self.segment[2 * a1] + self.segment[2 * a1 + 1]

    def sumRange(self, a1, a2):
        return self._range_query(1, 0, self.length - 1, a1, a2)

    def _range_query(self, a1, a2, a3, a4, a5):
        if a5 < a2 or a3 < a4:
            return 0
        if a4 <= a2 and a3 <= a5:
            return self.segment[a1]
        v1 = (a2 + a3) // 2
        v2 = self._range_query(2 * a1, a2, v1, a4, a5)
        v3 = self._range_query(2 * a1 + 1, v1 + 1, a3, a4, a5)
        return v2 + v3
