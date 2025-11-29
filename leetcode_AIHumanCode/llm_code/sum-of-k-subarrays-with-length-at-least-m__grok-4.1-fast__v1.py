class Solution(object):
    def maxSum(self, nums, k, m):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        prev = [0] * (n + 1)
        for _ in range(k):
            curr = [float('-inf')] * (n + 1)
            best = float('-inf')
            pos = -1
            for j in range(1, n + 1):
                curr[j] = curr[j - 1]
                if j >= m:
                    while pos < j - m:
                        pos += 1
                        best = max(best, prev[pos] - prefix[pos])
                    curr[j] = max(curr[j], prefix[j] + best)
            prev = curr
        return max(prev)
