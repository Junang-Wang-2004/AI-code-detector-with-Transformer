class Solution:
    def maxSubarrayLength(self, nums):
        n = len(nums)
        order = sorted(range(n), key=lambda k: -nums[k])
        result = 0
        p = n - 1
        for begin in range(n):
            while p >= 0 and nums[order[p]] < nums[begin]:
                j = order[p]
                if j > begin:
                    result = max(result, j - begin + 1)
                p -= 1
        return result
