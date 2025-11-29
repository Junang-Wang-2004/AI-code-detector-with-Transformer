# Time:  O(2^n)
# Space: O(1)

class Solution2(object):
    def grayCode(self, n):
        """
        """
        return [i >> 1 ^ i for i in range(1 << n)]


