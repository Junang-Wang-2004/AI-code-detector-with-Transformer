# Time:  O(nlogn)
# Space: O(1)
class Solution2(object):
    def eraseOverlapIntervals(self, intervals):
        """
        """
        intervals.sort(key=lambda interval: interval[0])
        result, prev = 0, 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[prev][1]:
                if intervals[i][1] < intervals[prev][1]:
                    prev = i
                result += 1
            else:
                prev = i
        return result

