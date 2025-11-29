import collections

class Solution(object):
    def unequalTriplets(self, nums):
        freq = collections.Counter(nums)
        total = len(nums)
        res = total * (total - 1) * (total - 2) // 6
        all_same = sum(f * (f - 1) * (f - 2) // 6 for f in freq.values())
        two_same = sum(f * (f - 1) // 2 * (total - f) for f in freq.values())
        return res - all_same - two_same
