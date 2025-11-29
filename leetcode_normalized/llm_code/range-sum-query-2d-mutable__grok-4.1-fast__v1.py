class C1:

    def __init__(self, a1):
        self.row_count = self.col_count = 0
        self.original_values = []
        self.fenwick_tree = []
        if not a1 or not a1[0]:
            return
        self.row_count = len(a1)
        self.col_count = len(a1[0])
        self.original_values = [list(row) for v1 in a1]
        self.fenwick_tree = [[0] * (self.col_count + 1) for v2 in range(self.row_count + 1)]
        for v3 in range(self.row_count):
            for v4 in range(self.col_count):
                self._modify(v3, v4, self.original_values[v3][v4])

    def update(self, a1, a2, a3):
        v1 = a3 - self.original_values[a1][a2]
        self.original_values[a1][a2] = a3
        if v1:
            self._modify(a1, a2, v1)

    def sumRegion(self, a1, a2, a3, a4):

        def prefix_sum(a1, a2):
            v1 = 0
            a1 += 1
            a2 += 1
            v4 = a1
            while v4 > 0:
                v5 = a2
                while v5 > 0:
                    v1 += self.fenwick_tree[v4][v5]
                    v5 -= v5 & -v5
                v4 -= v4 & -v4
            return v1
        return prefix_sum(a3, a4) - prefix_sum(a3, a2 - 1) - prefix_sum(a1 - 1, a4) + prefix_sum(a1 - 1, a2 - 1)

    def _modify(self, a1, a2, a3):
        v1 = a1 + 1
        v2 = a2 + 1
        v3 = self.row_count
        v4 = self.col_count
        while v1 <= v3:
            v5 = v2
            while v5 <= v4:
                self.fenwick_tree[v1][v5] += a3
                v5 += v5 & -v5
            v1 += v1 & -v1
