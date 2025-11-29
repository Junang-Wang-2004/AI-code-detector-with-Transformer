class Solution:
    def numSubseq(self, nums, target):
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        answer = 0
        for i in range(n):
            l, r = i, n - 1
            while l <= r:
                m = (l + r) // 2
                if nums[i] + nums[m] <= target:
                    l = m + 1
                else:
                    r = m - 1
            j = r
            if j >= i:
                answer = (answer + pow(2, j - i, MOD)) % MOD
        return answer
