class Solution:
    def maxNumOfMarkedIndices(self, nums):
        nums.sort()
        n = len(nums)
        pairs = 0
        large = n // 2
        for small in range(n // 2):
            while large < n and nums[large] < 2 * nums[small]:
                large += 1
            if large < n:
                pairs += 1
                large += 1
        return pairs * 2
