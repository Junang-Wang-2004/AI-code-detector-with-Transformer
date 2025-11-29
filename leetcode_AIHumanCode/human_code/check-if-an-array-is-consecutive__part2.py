# Time:  O(nlogn)
# Space: O(1)
# sort
class Solution2(object):
    def isConsecutive(self, nums):
        """
        """
        nums.sort()
        return all(nums[i]+1 == nums[i+1] for i in range(len(nums)-1))
