class Solution:
    def resultsArray(self, nums, k):
        n = len(nums)
        ans = [-1] * (n - k + 1)
        idx = 0
        while idx < n:
            end = idx
            while end + 1 < n and nums[end + 1] == nums[end] + 1:
                end += 1
            length = end - idx + 1
            if length >= k:
                for st in range(idx, end - k + 2):
                    ans[st] = nums[st + k - 1]
            idx = end + 1
        return ans
