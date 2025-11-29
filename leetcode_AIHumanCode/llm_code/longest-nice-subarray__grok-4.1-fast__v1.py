class Solution:
    def longestNiceSubarray(self, nums):
        ans = 0
        l = 0
        prev = [-1] * 32
        for r in range(len(nums)):
            max_prev = -1
            x = nums[r]
            b = 0
            while (1 << b) <= x:
                if x & (1 << b):
                    max_prev = max(max_prev, prev[b])
                b += 1
            l = max(l, max_prev + 1)
            b = 0
            while (1 << b) <= x:
                if x & (1 << b):
                    prev[b] = r
                b += 1
            ans = max(ans, r - l + 1)
        return ans
