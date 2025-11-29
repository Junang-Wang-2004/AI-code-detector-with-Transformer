# Time:  O(n)
# Space: O(1)

# dp, math
class Solution(object):
    def evenProduct(self, nums):
        """
        """
        result = (len(nums)+1)*len(nums)//2
        cnt = 0
        for x in nums:
            cnt = cnt+1 if x%2 else 0
            result -= cnt
        return result


