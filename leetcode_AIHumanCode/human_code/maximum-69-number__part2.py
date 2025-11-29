# Time:  O(logn)
# Space: O(logn)
class Solution2(object):
    def maximum69Number (self, num):
        """
        """
        return int(str(num).replace('6', '9', 1))
