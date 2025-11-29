# Time:  O(nlogn)
# Space: O(logn)
class Solution2(object):
    def getNoZeroIntegers(self, n):
        """
        """
        return next([a, n-a] for a in range(1, n) if '0' not in '{}{}'.format(a, n-a))
