# Time:  O(n)
# Space: O(1)

# sort, bitmasks, constructive algorithms
class Solution(object):
    def sortPermutation(self, nums):
        """
        """
        result = -1
        for i in range(len(nums)):
            if nums[i] == i:
                continue
            result = result&i if result != -1 else i
        return result if result != -1 else 0
