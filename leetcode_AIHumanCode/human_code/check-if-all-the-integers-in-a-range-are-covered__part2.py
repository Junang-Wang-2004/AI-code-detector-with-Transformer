# Time:  O(nlogn)
# Space: O(1)
# if r is big, this is better
class Solution2(object):
    def isCovered(self, ranges, left, right):
        """
        """
        ranges.sort()
        for l, r in ranges:
            if l <= left <= r:
                left = r+1
        return left > right


