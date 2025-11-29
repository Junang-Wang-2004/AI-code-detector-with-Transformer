class C1:

    def __init__(self, a1: int, a2: int):
        self.n = a1
        self.ninf = -float('inf')
        self.tree = [[0, 0] for v1 in range(4 * a1)]
        self._build(1, 0, a1 - 1, a2)

    def _build(self, a1: int, a2: int, a3: int, a4: int):
        if a2 == a3:
            self.tree[a1] = [a4, a4]
            return
        v1 = (a2 + a3) // 2
        self._build(2 * a1, a2, v1, a4)
        self._build(2 * a1 + 1, v1 + 1, a3, a4)
        v2 = self.tree[2 * a1]
        v3 = self.tree[2 * a1 + 1]
        self.tree[a1] = [max(v2[0], v3[0]), v2[1] + v3[1]]

    def update(self, a1: int, a2: int):
        self._update(1, 0, self.n - 1, a1, a2)

    def _update(self, a1: int, a2: int, a3: int, a4: int, a5: int):
        if a2 == a3:
            self.tree[a1] = [a5, a5]
            return
        v1 = (a2 + a3) // 2
        if a4 <= v1:
            self._update(2 * a1, a2, v1, a4, a5)
        else:
            self._update(2 * a1 + 1, v1 + 1, a3, a4, a5)
        v2 = self.tree[2 * a1]
        v3 = self.tree[2 * a1 + 1]
        self.tree[a1] = [max(v2[0], v3[0]), v2[1] + v3[1]]

    def range_query(self, a1: int, a2: int):
        return self._query(1, 0, self.n - 1, a1, a2)

    def _query(self, a1: int, a2: int, a3: int, a4: int, a5: int):
        if a4 > a3 or a5 < a2:
            return [self.ninf, 0]
        if a4 <= a2 and a3 <= a5:
            return self.tree[a1]
        v1 = (a2 + a3) // 2
        v2 = self._query(2 * a1, a2, v1, a4, a5)
        v3 = self._query(2 * a1 + 1, v1 + 1, a3, a4, a5)
        return [max(v2[0], v3[0]), v2[1] + v3[1]]

    def find_leftmost_ge(self, a1: int, a2: int):
        v1 = self.n + 1

        def dfs(a1: int, a2: int, a3: int):
            nonlocal ans
            if v1 <= a1:
                return
            if self.tree[a1][0] < a2:
                return
            if a2 == a3:
                v1 = a2
                return
            v2 = (a2 + a3) // 2
            dfs(2 * a1, a2, v2)
            dfs(2 * a1 + 1, v2 + 1, a3)
        dfs(1, 0, self.n - 1)
        return v1 if v1 <= a1 else -1

class C2:

    def __init__(self, a1: int, a2: int):
        self.seg_tree = C1(a1, a2)
        self.row_capacity = a2
        self.first_row = 0

    def gather(self, a1: int, a2: int) -> list[int]:
        v1 = self.seg_tree.find_leftmost_ge(a2, a1)
        if v1 == -1:
            return []
        v2 = self.seg_tree.range_query(v1, v1)[0]
        v3 = self.row_capacity - v2
        self.seg_tree.update(v1, v2 - a1)
        return [v1, v3]

    def scatter(self, a1: int, a2: int) -> bool:
        if a1 == 0:
            return True
        v1 = self.seg_tree.range_query(self.first_row, a2)[1]
        if v1 < a1:
            return False
        v2 = a1
        v3 = self.first_row
        while v2 > 0 and v3 <= a2:
            v4 = self.seg_tree.range_query(v3, v3)[0]
            v5 = min(v4, v2)
            self.seg_tree.update(v3, v4 - v5)
            v2 -= v5
