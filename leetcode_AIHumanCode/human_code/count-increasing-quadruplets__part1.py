# Time:  O(n^2)
# Space: O(n)

# dp
class Solution(object):
    def countQuadruplets(self, nums):
        """
        """
        dp = [0]*len(nums)  # dp[j] at l: # of tuple (i, j, k) s.t. i < j < k < l and nums[i] < nums[k] < nums[j]
        result = 0
        for l in range(len(nums)):
            cnt = 0
            for j in range(l):
                if nums[j] < nums[l]:
                    cnt += 1
                    result += dp[j]
                elif nums[j] > nums[l]:
                    dp[j] += cnt
        return result

    
