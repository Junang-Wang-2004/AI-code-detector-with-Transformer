from functools import reduce
# Time:  O(n)
# Space: O(1)

# bit manipulation
class Solution(object):
    def minOperations(self, nums, k):
        """
        """
        def popcount(x):
            return bin(x).count('1')
    
        return popcount(reduce(lambda x, y: x^y, nums, k))
