# Time:  O(logn)
# Space: O(1)

# bit manipulation
class Solution(object):
    def minChanges(self, n, k):
        """
        """
        def popcount(x):
            return bin(x).count('1')

        return popcount(n^k) if n&k == k else -1


