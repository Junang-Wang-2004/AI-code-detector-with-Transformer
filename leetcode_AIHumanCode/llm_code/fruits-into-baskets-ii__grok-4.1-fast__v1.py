class Solution(object):
    def numOfUnplacedFruits(self, fruit_sizes, cap):
        m = len(fruit_sizes)
        n = len(cap)
        if n == 0:
            return m
        tree = [0] * (4 * n)

        def construct(node, lo, hi):
            if lo == hi:
                tree[node] = cap[lo]
                return
            md = (lo + hi) // 2
            construct(2 * node, lo, md)
            construct(2 * node + 1, md + 1, hi)
            tree[node] = max(tree[2 * node], tree[2 * node + 1])

        def modify(node, lo, hi, idx, val):
            if lo == hi:
                tree[node] = val
                return
            md = (lo + hi) // 2
            if idx <= md:
                modify(2 * node, lo, md, idx, val)
            else:
                modify(2 * node + 1, md + 1, hi, idx, val)
            tree[node] = max(tree[2 * node], tree[2 * node + 1])

        def get_max(node, lo, hi, ql, qr):
            if qr < lo or hi < ql:
                return 0
            if ql <= lo and hi <= qr:
                return tree[node]
            md = (lo + hi) // 2
            left_max = get_max(2 * node, lo, md, ql, qr)
            right_max = get_max(2 * node + 1, md + 1, hi, ql, qr)
            return max(left_max, right_max)

        construct(1, 0, n - 1)
        unplaced = 0
        for size in fruit_sizes:
            l, r = 0, n - 1
            candidate = -1
            while l <= r:
                md = (l + r) // 2
                if get_max(1, 0, n - 1, 0, md) >= size:
                    candidate = md
                    r = md - 1
                else:
                    l = md + 1
            if candidate == -1:
                unplaced += 1
            else:
                modify(1, 0, n - 1, candidate, 0)
        return unplaced
