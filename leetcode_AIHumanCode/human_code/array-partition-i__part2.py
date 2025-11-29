# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
    def arrayPairSum(self, nums):
        """
        """
        nums.sort()
        result = 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        return result


