from functools import reduce
# Time:  O(n^2)
# Space: O(1)
# brute force
class Solution2(object):
    def minimumSubarrayLength(self, nums, k):
        """
        """
        result = float("inf")
        for left in range(len(nums)):
            curr = 0
            for right in range(left, len(nums)):
                curr |= nums[right]
                if curr < k:
                    continue
                result = min(result, right-left+1)
                break
        return result if result != float("inf") else -1
    
