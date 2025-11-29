class Solution:
    def beautifulPair(self, nums1, nums2):
        n = len(nums1)
        INF = 10**20
        seen = {}
        for i in range(n):
            pos = (nums1[i], nums2[i])
            if pos in seen:
                return [seen[pos], i]
            seen[pos] = i

        idxs = list(range(n))
        idxs.sort(key=lambda x: nums1[x])
        all_ys = sorted(set(nums2))
        ymap = {y: r for r, y in enumerate(all_ys)}
        m = len(all_ys)

        class SegTree:
            def __init__(self, sz):
                self.sz = sz
                self.tree = [(-INF, -1)] * (4 * sz)

            def _max(self, a, b):
                return max(a, b)

            def update(self, pos, val, idxx, node=1, start=0, end=None):
                if end is None:
                    end = self.sz - 1
                if start == end:
                    if val > self.tree[node][0]:
                        self.tree[node] = (val, idxx)
                    return
                mid = (start + end) // 2
                if pos <= mid:
                    self.update(pos, val, idxx, node * 2, start, mid)
                else:
                    self.update(pos, val, idxx, node * 2 + 1, mid + 1, end)
                self.tree[node] = self._max(self.tree[node * 2], self.tree[node * 2 + 1])

            def query(self, left, right, node=1, start=0, end=None):
                if end is None:
                    end = self.sz - 1
                if left > end or right < start:
                    return (-INF, -1)
                if left <= start and end <= right:
                    return self.tree[node]
                mid = (start + end) // 2
                l = self.query(left, right, node * 2, start, mid)
                r = self.query(left, right, node * 2 + 1, mid + 1, end)
                return self._max(l, r)

        stu = SegTree(m)
        stv = SegTree(m)

        def get_dist(i, j):
            d = abs(nums1[i] - nums1[j]) + abs(nums2[i] - nums2[j])
            return d, min(i, j), max(i, j)

        min_d = float('inf')
        ans_i = ans_j = -1
        for k in idxs:
            ry = ymap[nums2[k]]
            if ry > 0:
                mu, j = stu.query(0, ry - 1)
                if mu > -INF:
                    d, pi, pj = get_dist(k, j)
                    if d < min_d:
                        min_d = d
                        ans_i, ans_j = pi, pj
            mv, j = stv.query(ry, m - 1)
            if mv > -INF:
                d, pi, pj = get_dist(k, j)
                if d < min_d:
                    min_d = d
                    ans_i, ans_j = pi, pj
            stu.update(ry, nums1[k] + nums2[k], k)
            stv.update(ry, nums1[k] - nums2[k], k)
        return [ans_i, ans_j]
