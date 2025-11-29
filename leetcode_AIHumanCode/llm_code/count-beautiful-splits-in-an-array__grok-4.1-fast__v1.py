class Solution:
    def beautifulSplits(self, nums):
        n = len(nums)
        if n < 3:
            return 0
        suffix_lcp = [[0] * n for _ in range(n)]
        for delta in range(1, n):
            for p in range(n - delta - 1, -1, -1):
                q = p + delta
                if nums[p] == nums[q]:
                    addon = suffix_lcp[p + 1][q + 1] if q + 1 < n else 0
                    suffix_lcp[p][q] = 1 + addon
        ans = 0
        for a in range(1, n - 1):
            for b in range(a + 1, n):
                l1 = a
                l2 = b - a
                ok1 = suffix_lcp[0][a] >= l1 and l2 >= l1
                ok2 = suffix_lcp[a][b] >= l2
                if ok1 or ok2:
                    ans += 1
        return ans
