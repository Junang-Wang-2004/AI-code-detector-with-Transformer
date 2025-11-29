# Time:  O(n)
# Space: O(1)

# greedy
class Solution(object):
    def maximumPossibleSize(self, nums):
        """
        """
        result = prev = 0
        for x in nums:
            if prev <= x:
                prev = x
                result += 1
        return result
