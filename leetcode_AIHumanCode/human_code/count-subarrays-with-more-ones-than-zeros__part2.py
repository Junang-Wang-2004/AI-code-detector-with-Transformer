# Time:  O(n)
# Space: O(n)
class Solution2(object):
    def subarraysWithMoreZerosThanOnes(self, nums):
        """
        """
        MOD = 10**9+7

        lookup = {0:-1}
        dp = [0]*len(nums)
        result = total = 0
        for i, x in enumerate(nums):
            total += 1 if x == 1 else -1
            if total not in lookup:
                if total > 0:
                    dp[i] = i+1
            else:
                j = lookup[total]
                if j != -1:
                    dp[i] = dp[j]
                if x > 0:
                    dp[i] += (i-1)-j
            lookup[total] = i
            result = (result+dp[i])%MOD
        return result
