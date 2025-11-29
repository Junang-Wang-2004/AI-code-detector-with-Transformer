from sortedcontainers import SortedList
import collections

class C1(object):

    def findXSum(self, a1, a2, a3):
        v1 = collections.Counter()
        v2 = SortedList()
        v3 = 0
        v4 = []
        v5 = 0

        def add_upd(a1):
            nonlocal cur
            v1 = (-v1[a1], -a1)
            v2.add(v1)
            v2 = v2.index(v1)
            if v2 < a3:
                v3 += v1[a1] * a1
                if a3 < len(v2):
                    v4, v5 = v2[a3]
                    v3 -= v4 * v5

        def rem_upd(a1):
            nonlocal cur
            v1 = (-v1[a1], -a1)
            v2 = v2.index(v1)
            if v2 < a3:
                v3 -= v1[a1] * a1
                if a3 < len(v2):
                    v4, v5 = v2[a3]
                    v3 += v4 * v5
            v2.remove(v1)
        for v6 in range(len(a1)):
            v7 = a1[v6]
            if v1[v7] > 0:
                rem_upd(v7)
            v1[v7] += 1
            add_upd(v7)
            if v6 >= a2 - 1:
                v4.append(v3)
                v8 = a1[v5]
                rem_upd(v8)
                v1[v8] -= 1
                if v1[v8] > 0:
                    add_upd(v8)
                else:
                    del v1[v8]
                v5 += 1
        return v4
