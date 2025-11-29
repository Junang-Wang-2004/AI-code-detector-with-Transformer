# Time:  O(nlogn)
# Space: O(1)

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        """
        intervals.sort(key=lambda interval: interval[1])
        result, right = 0, float("-inf")
        for l, r in intervals:
            if l < right:
                result += 1
            else:
                right = r
        return result


