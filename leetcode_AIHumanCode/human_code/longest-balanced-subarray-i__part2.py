# Time:  O(n^2)
# Space: O(n)
# brute force
class Solution2(object):
    def longestBalanced(self, nums):
        """
        """
        result = 0
        for left in range(len(nums)):
            curr = 0
            lookup = set()
            for right in range(left, len(nums)):
                if nums[right] not in lookup:
                    lookup.add(nums[right])
                    curr += 1 if nums[right]&1 else -1
                if curr == 0:
                    result = max(result, right-left+1)
        return result
