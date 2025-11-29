class Solution:
    def countWays(self, nums):
        s = sorted(nums)
        n = len(s)
        ans = 0
        for pos in range(n + 1):
            left_valid = pos == 0 or s[pos - 1] < pos
            right_valid = pos == n or s[pos] > pos
            if left_valid and right_valid:
                ans += 1
        return ans
