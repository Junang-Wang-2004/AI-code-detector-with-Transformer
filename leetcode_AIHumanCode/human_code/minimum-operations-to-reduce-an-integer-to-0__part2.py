# Time:  O(logn)
# Space: O(1)
# greedy
class Solution2(object):
    def minOperations(self, n):
        """
        """
        result = 0
        while n:
            if n&1:
                n >>= 1
                n += n&1
                result += 1
            n >>= 1
        return result
