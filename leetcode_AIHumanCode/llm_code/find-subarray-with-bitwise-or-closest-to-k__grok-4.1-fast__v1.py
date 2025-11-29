class Solution:
    def minimumDifference(self, nums, k):
        ans = float('inf')
        states = set()
        for val in nums:
            ans = min(ans, abs(val - k))
            fresh = set([val])
            for prior in states:
                merged = prior | val
                fresh.add(merged)
                ans = min(ans, abs(merged - k))
            states = fresh
        return ans
