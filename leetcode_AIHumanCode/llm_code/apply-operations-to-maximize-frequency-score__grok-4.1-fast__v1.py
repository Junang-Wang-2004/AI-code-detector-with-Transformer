class Solution(object):
    def maxFrequencyScore(self, nums, k):
        nums.sort()
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        def get_cost(l, r):
            length = r - l + 1
            p = l + length // 2
            q = l + (length + 1) // 2
            sleft = prefix[p] - prefix[l]
            sright = prefix[r + 1] - prefix[q]
            return sright - sleft
        left = 0
        ans = 0
        for right in range(n):
            while left <= right and get_cost(left, right) > k:
                left += 1
            ans = max(ans, right - left + 1)
        return ans
