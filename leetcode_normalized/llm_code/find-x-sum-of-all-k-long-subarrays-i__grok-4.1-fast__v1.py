from sortedcontainers import SortedList
import collections

class C1(object):

    def findXSum(self, a1, a2, a3):
        v1 = {}
        v2 = SortedList()
        v3 = []
        v4 = 0

        def increment(a1):
            nonlocal cur_sum
            v1 = v1.get(a1, 0)
            v2 = v1 + 1
            v1[a1] = v2
            if v1 > 0:
                v3 = (-v1, -a1)
                v4 = v2.index(v3)
                if v4 < a3:
                    v5 -= v1 * a1
                if len(v2) > a3:
                    v6, v7 = v2[a3]
                    v5 += -v6 * -v7
                v2.remove(v3)
            v8 = (-v2, -a1)
            v2.add(v8)
            v4 = v2.index(v8)
            if v4 < a3:
                v5 += v2 * a1
            if len(v2) > a3:
                v6, v7 = v2[a3]
                v5 -= -v6 * -v7

        def decrement(a1):
            nonlocal cur_sum
            v1 = v1[a1]
            v2 = v1 - 1
            v1[a1] = v2
            v3 = (-v1, -a1)
            v4 = v2.index(v3)
            if v4 < a3:
                v5 -= v1 * a1
            if len(v2) > a3:
                v6, v7 = v2[a3]
                v5 += -v6 * -v7
            v2.remove(v3)
            if v2 > 0:
                v8 = (-v2, -a1)
                v2.add(v8)
                v4 = v2.index(v8)
                if v4 < a3:
                    v5 += v2 * a1
                if len(v2) > a3:
                    v6, v7 = v2[a3]
                    v5 -= -v6 * -v7
            else:
                del v1[a1]
        v5 = len(a1)
        for v6 in range(v5):
            increment(a1[v6])
            if v6 >= a2 - 1:
                v3.append(v4)
                v7 = a1[v6 - a2 + 1]
                decrement(v7)
        return v3
