# Time:  O(nlogn)
# Space: O(1)
# sort, greedy, two pointers
class Solution2(object):
    def maximizeGreatness(self, nums):
        """
        """
        nums.sort()
        left = 0
        for right in range(len(nums)):
            if nums[right] > nums[left]:
                left += 1
        return left
