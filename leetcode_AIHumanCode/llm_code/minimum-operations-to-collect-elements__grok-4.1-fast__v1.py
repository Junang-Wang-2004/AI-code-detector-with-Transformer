class Solution(object):
    def minOperations(self, nums, k):
        found = set()
        n = len(nums)
        for pos in range(n - 1, -1, -1):
            if nums[pos] <= k:
                found.add(nums[pos])
            if len(found) == k:
                return n - pos
        return n
