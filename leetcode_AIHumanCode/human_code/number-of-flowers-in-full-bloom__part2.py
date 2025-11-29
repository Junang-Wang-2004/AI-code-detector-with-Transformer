# Time:  O(nlogn + mlogn)
# Space: O(n)
import bisect


# binary search
class Solution(object):
    def fullBloomFlowers(self, flowers, persons):
        """
        """
        starts, ends = [], []
        for s, e in flowers:
            starts.append(s)
            ends.append(e+1)
        starts.sort()
        ends.sort()
        return [bisect.bisect_right(starts, t)-bisect.bisect_right(ends, t) for t in persons]
