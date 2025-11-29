# Time:  O(logn)
# Space: O(1)
# bit manipulation
class Solution2(object):
    def minChanges(self, n, k):
        """
        """
        def popcount(x):
            return bin(x).count('1')

        return popcount(n^k) if n|(n^k) == n else -1
