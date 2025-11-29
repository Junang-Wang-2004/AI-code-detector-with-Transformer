# Time:  O(n)
# Space: O(n)

nums = [0, 1]
dp = [0, 1]
class Solution(object):
    def getMaximumGenerated(self, n):
        """
        """
        if n+1 > len(dp):
            for i in range(len(nums), n+1):
                if i%2 == 0:
                    nums.append(nums[i//2])
                else:
                    nums.append(nums[i//2] + nums[i//2+1])
                dp.append(max(dp[-1], nums[-1]))
        return dp[n]


