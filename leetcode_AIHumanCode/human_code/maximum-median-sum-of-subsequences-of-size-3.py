# Time:  O(nlogn)
# Space: O(1)

# sort, greedy
class Solution(object):
    def maximumMedianSum(self, nums):
        """
        """
        nums.sort()
        return sum(nums[i] for i in range(len(nums)//3, len(nums), 2))
