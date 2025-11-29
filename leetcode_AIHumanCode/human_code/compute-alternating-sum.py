# Time:  O(n)
# Space: O(1)

# array
class Solution(object):
    def alternatingSum(self, nums):
        """
        """
        return sum(nums[i] for i in range(0, len(nums), 2))-sum(nums[i] for i in range(1, len(nums), 2))
