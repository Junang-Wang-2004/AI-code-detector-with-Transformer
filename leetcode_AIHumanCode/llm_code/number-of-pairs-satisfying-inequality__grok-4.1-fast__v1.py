import bisect

class Solution:
    def numberOfPairs(self, nums1, nums2, diff):
        n = len(nums1)
        vals = [nums1[i] - nums2[i] for i in range(n)]
        coords = sorted(set(vals))
        m = len(coords)
        mapping = {coords[j]: j for j in range(m)}
        tree = [0] * (m + 2)
        def modify(pos, delta):
            pos += 1
            while pos <= m:
                tree[pos] += delta
                pos += pos & -pos
        def inquire(pos):
            pos += 1
            total = 0
            while pos > 0:
                total += tree[pos]
                pos -= pos & -pos
            return total
        count = 0
        for v in vals:
            idx = bisect.bisect_right(coords, v + diff) - 1
            if idx >= 0:
                count += inquire(idx)
            modify(mapping[v], 1)
        return count
