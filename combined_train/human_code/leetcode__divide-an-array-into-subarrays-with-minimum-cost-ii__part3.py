from sortedcontainers import SortedList

class C1(object):

    def minimumCost(self, a1, a2, a3):
        """
        """
        v1, v2 = (SortedList(), SortedList())
        v3, v4 = (float('inf'), 0)
        for v5 in range(1, len(a1)):
            v1.add(a1[v5])
            v4 += a1[v5]
            if len(v1) > a2 - 1:
                v4 -= v1[-1]
                v2.add(v1.pop())
            if len(v1) + len(v2) > 1 + a3:
                if v2[0] <= a1[v5 - (1 + a3)]:
                    v2.remove(a1[v5 - (1 + a3)])
                else:
                    v1.remove(a1[v5 - (1 + a3)])
                    v4 -= a1[v5 - (1 + a3)] - v2[0]
                    v1.add(v2.pop(0))
            if len(v1) == a2 - 1:
                v3 = min(v3, v4)
        return a1[0] + v3
