import collections

class Solution:
    def minGroupsForValidAssignment(self, nums):
        cnt = collections.Counter(nums)
        freqs = list(cnt.values())
        if not freqs:
            return 0
        lo = min(freqs)
        for k in range(lo, 0, -1):
            m = k + 1
            gs = [(f + m - 1) // m for f in freqs]
            if all(g * k <= f for f, g in zip(freqs, gs)):
                return sum(gs)
        return 0
