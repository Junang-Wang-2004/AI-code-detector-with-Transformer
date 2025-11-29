# Time:  O(nlogn + mlogn)
# Space: O(n)

import bisect


# line sweep, binary search
class Solution(object):
    def fullBloomFlowers(self, flowers, persons):
        """
        """
        cnt = collections.Counter()
        for s, e in flowers:
            cnt[s] += 1
            cnt[e+1] -= 1
        events = sorted(cnt.keys())
        prefix = [0]
        for x in events:
            prefix.append(prefix[-1]+cnt[x])
        return [prefix[bisect.bisect_right(events, t)] for t in persons]


