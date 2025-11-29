import bisect

class Solution(object):
    def makeArrayIncreasing(self, nums1, nums2):
        opts = sorted(set(nums2))
        m = len(nums1)
        INF = 10**18 + 42
        ends = [-1] + [INF] * m
        for num in nums1:
            new_ends = [INF] * (m + 1)
            for c in range(m + 1):
                prev = ends[c]
                if prev == INF:
                    continue
                if prev < num:
                    new_ends[c] = min(new_ends[c], num)
                pos = bisect.bisect_right(opts, prev)
                if pos < len(opts):
                    nc = c + 1
                    if nc <= m:
                        new_ends[nc] = min(new_ends[nc], opts[pos])
            if all(e == INF for e in new_ends):
                return -1
            ends = new_ends
        for c in range(m + 1):
            if ends[c] != INF:
                return c
        return -1
