# Time:  O(nlogn)
# Space: O(n)
# sort
class Solution2(object):
    def maxSubarrayLength(self, nums):
        """
        """
        idxs = list(range(len(nums)))
        idxs.sort(key=lambda x: nums[x], reverse=True)
        result = 0
        for left in range(len(nums)):
            while idxs and nums[idxs[-1]] < nums[left]:
                result = max(result, idxs.pop()-left+1)
        return result
