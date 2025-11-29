# Time:  O(n)
# Space: O(1)
# greedy
class Solution2(object):
    def maximumOddBinaryNumber(self, s):
        """
        """
        n = s.count('1')
        return "".join(['1']*(n-1)+['0']*(len(s)-n)+['1'])
