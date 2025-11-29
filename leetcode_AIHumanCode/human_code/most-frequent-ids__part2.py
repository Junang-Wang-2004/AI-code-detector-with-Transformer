# Time:  O(nlogn)
# Space: O(n)
import collections
import itertools
from sortedcontainers import SortedList


# sorted list
class Solution2(object):
    def mostFrequentIDs(self, nums, freq):
        """
        """
        result = []
        cnt = collections.Counter()
        cnt2 = collections.Counter()
        sl = SortedList()
        for x, f in zip(nums, freq):
            sl.discard((cnt[x], cnt2[cnt[x]]))
            cnt2[cnt[x]] -= 1
            if cnt2[cnt[x]]:
                sl.add((cnt[x], cnt2[cnt[x]]))
            cnt[x] += f
            sl.discard((cnt[x], cnt2[cnt[x]]))
            cnt2[cnt[x]] += 1
            sl.add((cnt[x], cnt2[cnt[x]]))
            result.append(sl[-1][0])
        return result
