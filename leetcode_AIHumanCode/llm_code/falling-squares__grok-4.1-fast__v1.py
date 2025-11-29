import bisect

class SegTree:
    def __init__(self, nn):
        self.size = nn
        self.tree = [0] * (4 * nn)
        self.lazy = [float('-inf')] * (4 * nn)

    def propagate(self, node, start, end):
        if self.lazy[node] != float('-inf'):
            self.tree[node] = max(self.tree[node], self.lazy[node])
            if start != end:
                self.lazy[2 * node] = max(self.lazy[2 * node], self.lazy[node])
                self.lazy[2 * node + 1] = max(self.lazy[2 * node + 1], self.lazy[node])
            self.lazy[node] = float('-inf')

    def update(self, left, right, value, node=1, start=0, end=None):
        if end is None:
            end = self.size - 1
        self.propagate(node, start, end)
        if left > end or right < start:
            return
        if left <= start and end <= right:
            self.lazy[node] = max(self.lazy[node], value)
            self.propagate(node, start, end)
            return
        mid = (start + end) // 2
        self.update(left, right, value, 2 * node, start, mid)
        self.update(left, right, value, 2 * node + 1, mid + 1, end)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, left, right, node=1, start=0, end=None):
        if end is None:
            end = self.size - 1
        self.propagate(node, start, end)
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self.query(left, right, 2 * node, start, mid)
        p2 = self.query(left, right, 2 * node + 1, mid + 1, end)
        return max(p1, p2)


class Solution:
    def fallingSquares(self, positions):
        endpoints = set()
        for pos_left, pos_size in positions:
            endpoints.add(pos_left)
            endpoints.add(pos_left + pos_size - 1)
        coord_list = sorted(endpoints)
        num_coords = len(coord_list)
        height_tree = SegTree(num_coords)
        overall_max = 0
        output_list = []
        for pos_left, pos_size in positions:
            range_end = pos_left + pos_size - 1
            idx_left = bisect.bisect_left(coord_list, pos_left)
            idx_right = bisect.bisect_left(coord_list, range_end)
            range_max = height_tree.query(idx_left, idx_right)
            new_top = range_max + pos_size
            height_tree.update(idx_left, idx_right, new_top)
            overall_max = max(overall_max, new_top)
            output_list.append(overall_max)
        return output_list
