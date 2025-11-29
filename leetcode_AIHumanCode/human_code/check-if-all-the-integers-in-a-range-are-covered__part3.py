# Time:  O(n * r)
# Space: O(1)
class Solution3(object):
    def isCovered(self, ranges, left, right):
        """
        """
        return all(any(l <= i <= r for l, r in ranges) for i in range(left, right+1))
