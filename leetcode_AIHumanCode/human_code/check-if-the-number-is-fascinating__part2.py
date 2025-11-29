# Time:  O(logn)
# Space: O(logn)
# string
class Solution2(object):
    def isFascinating(self, n):
        """
        """
        s = str(n)+str(2*n)+str(3*n)
        return '0' not in s and len(s) == 9 and len(set(s)) == 9
