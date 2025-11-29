# Time:  O(n^2)
# Space: O(1)
# simulation
class Solution3(object):
    def triangularSum(self, nums):
        """
        """
        for i in reversed(range(len(nums))):
            for j in range(i):
                nums[j] = (nums[j]+nums[j+1])%10
        return nums[0]
