class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class SummaryRanges(object):

    def __init__(self):
        self._ranges = []

    def addNum(self, num):
        lo, hi = 0, len(self._ranges)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if self._ranges[mid][0] > num:
                hi = mid
            else:
                lo = mid + 1
        pos = lo
        merge_left = pos > 0 and self._ranges[pos - 1][1] + 1 >= num
        if merge_left:
            pos -= 1
            left_bound = self._ranges[pos][0]
            right_bound = max(self._ranges[pos][1], num)
        else:
            left_bound = num
            right_bound = num
        while pos < len(self._ranges) and self._ranges[pos][0] <= right_bound + 1:
            left_bound = min(left_bound, self._ranges[pos][0])
            right_bound = max(right_bound, self._ranges[pos][1])
            del self._ranges[pos]
        self._ranges.insert(pos, [left_bound, right_bound])

    def getIntervals(self):
        return [Interval(rng[0], rng[1]) for rng in self._ranges]
