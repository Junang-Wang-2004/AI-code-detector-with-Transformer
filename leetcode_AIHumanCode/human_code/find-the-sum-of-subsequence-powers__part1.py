# Time:  O(n^2 + len(diffs) * n * k) = O(n^3 * k) at most
# Space: O(len(diffs) + n * k) = O(n^2) at most

# sort, dp, prefix sum, two pointers
class Solution(object):
    def sumOfPowers(self, nums, k):
        MOD = 10**9+7
        nums.sort()
        result = prev = 0
        for mn in sorted({nums[j]-nums[i] for i in range(len(nums)) for j in range(i+1, len(nums))}, reverse=True):
            dp = [[0]*(k+1) for _ in range(len(nums)+1)]
            dp[0][0] = 1
            j = 0
            for i in range(len(nums)):
                j = next((j for j in range(j, len(nums)) if nums[i]-nums[j] < mn), len(nums))
                for l in range(1, k+1):
                    dp[i+1][l] = (dp[i+1][l]+dp[(j-1)+1][l-1])%MOD  # dp[i+1][l]: count of subsequences of length l ending at i having min diff >= mn
                for l in range(k+1):
                    dp[i+1][l] = (dp[i+1][l]+dp[i][l])%MOD  # dp[i+1][l]: accumulated count of subsequences of length l ending at [0, i] having min diff >= mn
            cnt = (dp[-1][k]-prev)%MOD
            result = (result+mn*cnt)%MOD
            prev = dp[-1][k]
        return result


