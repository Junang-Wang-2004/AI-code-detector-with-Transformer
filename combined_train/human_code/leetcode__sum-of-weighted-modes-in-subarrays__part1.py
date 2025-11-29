import collections
from sortedcontainers import SortedList

class C1(object):

    def modeWeight(self, a1, a2):
        """
        """

        def add(a1, a2):
            if cnt[a1]:
                sl.remove((-cnt[a1], a1))
            cnt[a1] += a2
            if cnt[a1]:
                sl.add((-cnt[a1], a1))
            else:
                del cnt[a1]
        v1 = collections.defaultdict(int)
        v2 = SortedList()
        v3 = 0
        for v4 in range(len(a1)):
            add(a1[v4], +1)
            if v4 >= a2 - 1:
                v3 += -v2[0][0] * v2[0][1]
                add(a1[v4 - a2 + 1], -1)
        return v3
