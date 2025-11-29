# Time:  O(n)
# Space: O(1)

# array
class Solution(object):
    def constructTransformedArray(self, nums):
        """
        """
        return [nums[(i+nums[i])%len(nums)] for i in range(len(nums))]
