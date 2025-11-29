# Time:  O(nlogn)
# Space: O(1)

# sort, greedy, two pointers
class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        """
        """
        nums.sort()
        left = 0
        for right in range((len(nums)+1)//2, len(nums)):
            if nums[right] >= 2*nums[left]:
                left += 1
        return left*2


