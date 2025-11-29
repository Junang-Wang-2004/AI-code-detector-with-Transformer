class Solution(object):
    def minChanges(self, nums, k):
        n = len(nums)
        pairs = n // 2
        diff_count = [0] * (k + 1)
        rad_count = [0] * (k + 1)
        for i in range(pairs):
            left = nums[i]
            right = nums[n - 1 - i]
            delta = abs(left - right)
            radius = max(left, k - left, right, k - right)
            diff_count[delta] += 1
            rad_count[radius] += 1
        less_count = [0] * (k + 2)
        accum = 0
        for v in range(k + 1):
            less_count[v] = accum
            accum += rad_count[v]
        ans = pairs
        for v in range(k + 1):
            cost = pairs - diff_count[v] + less_count[v]
            if cost < ans:
                ans = cost
        return ans
