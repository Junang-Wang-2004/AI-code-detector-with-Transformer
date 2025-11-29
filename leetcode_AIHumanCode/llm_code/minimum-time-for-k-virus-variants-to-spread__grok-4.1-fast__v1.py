class LazySegTree:
    def __init__(self, size):
        self.size = size
        self.data = [0] * (4 * size)
        self.lazy = [0] * (4 * size)

    def _push(self, idx, l, r):
        if self.lazy[idx]:
            self.data[idx] += self.lazy[idx]
            if l != r:
                self.lazy[2 * idx] += self.lazy[idx]
                self.lazy[2 * idx + 1] += self.lazy[idx]
            self.lazy[idx] = 0

    def _update(self, idx, l, r, ql, qr, val):
        self._push(idx, l, r)
        if ql > r or qr < l:
            return
        if ql <= l and r <= qr:
            self.lazy[idx] += val
            self._push(idx, l, r)
            return
        m = (l + r) // 2
        self._update(2 * idx, l, m, ql, qr, val)
        self._update(2 * idx + 1, m + 1, r, ql, qr, val)
        self.data[idx] = max(self.data[2 * idx], self.data[2 * idx + 1])

    def update_range(self, left, right, val):
        if self.size == 0:
            return
        self._update(1, 0, self.size - 1, left, right, val)

    def _query(self, idx, l, r, ql, qr):
        self._push(idx, l, r)
        if ql > r or qr < l:
            return float('-inf')
        if ql <= l and r <= qr:
            return self.data[idx]
        m = (l + r) // 2
        return max(
            self._query(2 * idx, l, m, ql, qr),
            self._query(2 * idx + 1, m + 1, r, ql, qr)
        )

    def get_max(self):
        if self.size == 0:
            return 0
        return self._query(1, 0, self.size - 1, 0, self.size - 1)


class Solution(object):
    def minDayskVariants(self, points, k):
        trans = [[x + y, x - y] for x, y in points]
        if not trans:
            return 0
        x_coords = [p[0] for p in trans]
        y_coords = [p[1] for p in trans]
        min_x = min(x_coords)
        max_x = max(x_coords)
        min_y = min(y_coords)
        max_y = max(y_coords)
        lo, hi = 0, ((max_x - min_x) + (max_y - min_y) + 1) // 2

        def can_cover(radius):
            events = []
            yset = set()
            for px, py in trans:
                lx = px - radius
                rx = px + radius + 1
                ly_ = py - radius
                hy_ = py + radius
                events.append((lx, 1, ly_, hy_))
                events.append((rx, -1, ly_, hy_))
                yset.add(ly_)
                yset.add(hy_)
            events.sort()
            ysorted = sorted(yset)
            ydict = {y: i for i, y in enumerate(ysorted)}
            ny = len(ysorted)
            seg = LazySegTree(ny)
            for _, dv, ly, hy in events:
                il = ydict[ly]
                ir = ydict[hy]
                seg.update_range(il, ir, dv)
                if seg.get_max() >= k:
                    return True
            return False

        while lo <= hi:
            md = lo + (hi - lo) // 2
            if can_cover(md):
                hi = md - 1
            else:
                lo = md + 1
        return lo
