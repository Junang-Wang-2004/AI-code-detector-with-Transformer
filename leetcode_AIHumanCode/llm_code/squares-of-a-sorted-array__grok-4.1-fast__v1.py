class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        ans = [0] * n
        i, j = 0, n - 1
        for k in range(n - 1, -1, -1):
            if nums[i] ** 2 > nums[j] ** 2:
                ans[k] = nums[i] ** 2
                i += 1
            else:
                ans[k] = nums[j] ** 2
                j -= 1
        return ans
