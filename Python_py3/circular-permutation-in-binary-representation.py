# Time:  O(2^n)
# Space: O(1)

class Solution(object):
    def circularPermutation(self, n, start):
        """
        """
        return [start ^ (i>>1) ^ i for i in range(1<<n)]
