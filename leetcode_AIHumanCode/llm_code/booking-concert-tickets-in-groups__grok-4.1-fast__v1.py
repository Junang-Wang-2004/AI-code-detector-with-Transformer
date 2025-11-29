class SegmentTree:
    def __init__(self, size: int, init_val: int):
        self.n = size
        self.ninf = -float('inf')
        self.tree = [[0, 0] for _ in range(4 * size)]
        self._build(1, 0, size - 1, init_val)

    def _build(self, node: int, start: int, end: int, val: int):
        if start == end:
            self.tree[node] = [val, val]
            return
        mid = (start + end) // 2
        self._build(2 * node, start, mid, val)
        self._build(2 * node + 1, mid + 1, end, val)
        left = self.tree[2 * node]
        right = self.tree[2 * node + 1]
        self.tree[node] = [max(left[0], right[0]), left[1] + right[1]]

    def update(self, pos: int, new_val: int):
        self._update(1, 0, self.n - 1, pos, new_val)

    def _update(self, node: int, start: int, end: int, pos: int, val: int):
        if start == end:
            self.tree[node] = [val, val]
            return
        mid = (start + end) // 2
        if pos <= mid:
            self._update(2 * node, start, mid, pos, val)
        else:
            self._update(2 * node + 1, mid + 1, end, pos, val)
        left = self.tree[2 * node]
        right = self.tree[2 * node + 1]
        self.tree[node] = [max(left[0], right[0]), left[1] + right[1]]

    def range_query(self, left: int, right: int):
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, node: int, start: int, end: int, qleft: int, qright: int):
        if qleft > end or qright < start:
            return [self.ninf, 0]
        if qleft <= start and end <= qright:
            return self.tree[node]
        mid = (start + end) // 2
        lres = self._query(2 * node, start, mid, qleft, qright)
        rres = self._query(2 * node + 1, mid + 1, end, qleft, qright)
        return [max(lres[0], rres[0]), lres[1] + rres[1]]

    def find_leftmost_ge(self, max_r: int, thresh: int):
        ans = self.n + 1
        def dfs(nd: int, s: int, e: int):
            nonlocal ans
            if ans <= max_r:
                return
            if self.tree[nd][0] < thresh:
                return
            if s == e:
                ans = s
                return
            mid = (s + e) // 2
            dfs(2 * nd, s, mid)
            dfs(2 * nd + 1, mid + 1, e)
        dfs(1, 0, self.n - 1)
        return ans if ans <= max_r else -1


class BookMyShow:
    def __init__(self, n: int, m: int):
        self.seg_tree = SegmentTree(n, m)
        self.row_capacity = m
        self.first_row = 0

    def gather(self, k: int, maxRow: int) -> list[int]:
        target_row = self.seg_tree.find_leftmost_ge(maxRow, k)
        if target_row == -1:
            return []
        curr_empty = self.seg_tree.range_query(target_row, target_row)[0]
        start_col = self.row_capacity - curr_empty
        self.seg_tree.update(target_row, curr_empty - k)
        return [target_row, start_col]

    def scatter(self, k: int, maxRow: int) -> bool:
        if k == 0:
            return True
        total_empty = self.seg_tree.range_query(self.first_row, maxRow)[1]
        if total_empty < k:
            return False
        remaining = k
        current_row = self.first_row
        while remaining > 0 and current_row <= maxRow:
            row_empty = self.seg_tree.range_query(current_row, current_row)[0]
            seats_to_book = min(row_empty, remaining)
            self.seg_tree.update(current_row, row_empty - seats_to_book)
            remaining -= seats_to_book
