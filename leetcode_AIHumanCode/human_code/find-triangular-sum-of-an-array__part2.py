# Time:  O(n^2)
# Space: O(n)
# combinatorics
class Solution2(object):
    def triangularSum(self, nums):
        """
        """
        result = 0
        nCr = 1
        for i in range(len(nums)):
            result = (result+nCr*nums[i])%10
            nCr *= (len(nums)-1)-i
            nCr //= i+1
        return result


