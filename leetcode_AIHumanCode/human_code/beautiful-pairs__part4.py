# Time:  O(nlogn)
# Space: O(n)
import itertools


# segment tree
class Solution4(object):
    def beautifulPair(self, nums1, nums2):
        """
        """
        INF = float("inf")
        # Range Maximum Query
        class SegmentTree(object):
            def __init__(self, N,
                         build_fn=lambda _: [-INF, -INF],  # modified
                         query_fn=lambda x, y: y if x is None else x if y is None else max(x, y),
                         update_fn=lambda x: x):
                self.tree = [None]*(2*2**((N-1).bit_length()))
                self.base = len(self.tree)//2
                self.query_fn = query_fn
                self.update_fn = update_fn
                for i in range(self.base, self.base+N):
                    self.tree[i] = build_fn(i-self.base)
                for i in reversed(range(1, self.base)):
                    self.tree[i] = query_fn(self.tree[2*i], self.tree[2*i+1])

            def update(self, i, h):
                x = self.base+i
                self.tree[x] = self.update_fn(h)
                while x > 1:
                    x //= 2
                    self.tree[x] = self.query_fn(self.tree[x*2], self.tree[x*2+1])

            def query(self, L, R):
                if L > R:
                    return [-INF, -INF]  # modified
                L += self.base
                R += self.base
                left = right = None
                while L <= R:
                    if L & 1:
                        left = self.query_fn(left, self.tree[L])
                        L += 1
                    if R & 1 == 0:
                        right = self.query_fn(self.tree[R], right)
                        R -= 1
                    L //= 2
                    R //= 2
                return self.query_fn(left, right)

        def dist(a, b):
            if a > b:
                a, b = b, a
            return [abs(points[a][0]-points[b][0])+abs(points[a][1]-points[b][1]), a, b]

        points = [(i, j) for i, j in zip(nums1, nums2)]
        result = [INF]*3
        lookup = {}
        for i in reversed(range(len(points))):
            if points[i] in lookup:
                result = [0, (i, lookup[points[i]])]
            lookup[points[i]] = i
        if result[0] == 0:
            return result[1]
        order = list(range(len(points)))
        order.sort(key=lambda x: points[x][0])
        y_set = set(y for _, y in points)
        y_to_idx = {y:i for i, y in enumerate(sorted(y_set))}
        st1, st2 = SegmentTree(len(y_to_idx)), SegmentTree(len(y_to_idx))
        for i in order:
            j = -st1.query(0, y_to_idx[points[i][1]]-1)[1]  # min((xi-xj)+(yi-yj) for j in range(y_to_idx[points[i][1])) = (xi+yi)-max((xj+yj) for j in range(y_to_idx[points[i][1]))
            if j != INF:
                assert(points[j][1] < points[i][1])
                result = min(result, dist(i, j))
            st1.update(y_to_idx[points[i][1]], [points[i][0]+points[i][1], -i])
            j = -st2.query(y_to_idx[points[i][1]], len(y_to_idx)-1)[1]  # min((xi-xj)+(yj-yi) for j in range(y_to_idx[points[i][1], len(y_to_idx))) = (xi-yi)-max((xj-yj) for j in range(y_to_idx[points[i][1], len(y_to_idx))
            if j != INF:
                assert(points[j][1] >= points[i][1])
                result = min(result, dist(i, j))
            st2.update(y_to_idx[points[i][1]], [points[i][0]-points[i][1], -i])
        return result[1:]
