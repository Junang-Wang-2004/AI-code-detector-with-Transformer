# Time:  O(logn)
# Space: O(1)
# math, bitmasks
class Solution2(object):
    def kthLuckyNumber(self, k):
        """
        """
        return bin(k+1)[3:].replace('1', '7').replace('0', '4')
