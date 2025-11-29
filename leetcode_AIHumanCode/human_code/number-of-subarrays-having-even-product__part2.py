# Time:  O(n)
# Space: O(1)
# dp, math
class Solution2(object):
    def evenProduct(self, nums):
        """
        """
        result = cnt = 0
        for i, x in enumerate(nums):
            if x%2 == 0:
                cnt = i+1
            result += cnt
        return result
