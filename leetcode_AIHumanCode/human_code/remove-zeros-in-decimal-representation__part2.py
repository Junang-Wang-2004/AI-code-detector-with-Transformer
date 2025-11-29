# Time:  O(logn)
# Space: O(logn)
# string
class Solution2(object):
    def removeZeros(self, n):
        """
        """
        result = "".join(x for x in str(n) if x != '0')
        return int(result) if result else 0
