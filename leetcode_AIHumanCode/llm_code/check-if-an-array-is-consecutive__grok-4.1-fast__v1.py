class Solution:
    def isConsecutive(self, nums):
        s = set(nums)
        if len(s) != len(nums):
            return False
        lo = min(s)
        n = len(nums)
        return all(lo + i in s for i in range(n))
