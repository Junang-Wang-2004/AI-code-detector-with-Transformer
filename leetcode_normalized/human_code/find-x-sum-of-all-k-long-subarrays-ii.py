from sortedcontainers import SortedList
import collections

class C1(object):

    def findXSum(self, a1, a2, a3):
        """
        """

        def update(a1, a2, a3):
            if a2 == 1:
                sl.add((-cnt[a1], -a1))
            if sl.index((-cnt[a1], -a1)) < a3:
                a3 += a2 * cnt[a1] * a1
                if a3 < len(sl):
                    v2, v3 = sl[a3]
                    a3 -= a2 * v2 * v3
            if a2 != 1:
                sl.remove((-cnt[a1], -a1))
            return a3
        v1 = SortedList()
        v2 = collections.defaultdict(int)
        v3 = []
        v4 = 0
        for v5, v6 in enumerate(a1):
            if v6 in v2:
                v4 = update(v6, -1, v4)
            v2[v6] += 1
            v4 = update(v6, +1, v4)
            if v5 < a2 - 1:
                continue
            v3.append(v4)
            v4 = update(a1[v5 - (a2 - 1)], -1, v4)
            v2[a1[v5 - (a2 - 1)]] -= 1
            if v2[a1[v5 - (a2 - 1)]]:
                v4 = update(a1[v5 - (a2 - 1)], +1, v4)
            else:
                del v2[a1[v5 - (a2 - 1)]]
        return v3
