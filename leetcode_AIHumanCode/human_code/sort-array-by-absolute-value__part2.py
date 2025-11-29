# Time:  O(nlogn)
# Space: O(1)
# sort
class Solution2(object):
    def sortByAbsoluteValue(self, nums):
        """
        """
        nums.sort(key=lambda x: abs(x))
        return nums
