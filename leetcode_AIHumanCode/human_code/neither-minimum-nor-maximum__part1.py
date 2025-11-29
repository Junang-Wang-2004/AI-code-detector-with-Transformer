# Time:  O(n)
# Space: O(1)

# one pass, array
class Solution(object):
    def findNonMinOrMax(self, nums):
        """
        """
        mx, mn = float("-inf"), float("inf")
        result = -1
        for x in nums:
            if mn < x < mx:
                return x
            if x < mn:
                result = mn
                mn = x
            if x > mx:
                result = mx
                mx = x
        return result if mn < result < mx else -1


