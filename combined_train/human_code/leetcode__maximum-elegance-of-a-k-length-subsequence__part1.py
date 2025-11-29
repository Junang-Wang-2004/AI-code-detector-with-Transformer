import heapq
from sortedcontainers import SortedList

class C1(object):

    def findMaximumElegance(self, a1, a2):
        """
        """
        v1 = 0
        v2 = set()
        v3 = []
        for v4, v5 in heapq.nlargest(a2, a1):
            if v5 in v2:
                v3.append(v4)
            v1 += v4
            v2.add(v5)
        v6 = SortedList()
        v7 = {}
        for v4, v5 in a1:
            if v5 in v2:
                continue
            if v5 in v7:
                if v7[v5] >= v4:
                    continue
                v6.remove((v7[v5], v5))
            v6.add((v4, v5))
            v7[v5] = v4
            if len(v6) > len(v3):
                del v7[v6[0][1]]
                del v6[0]
        v8 = v1 + len(v2) ** 2
        for v4, v5 in reversed(v6):
            v1 += v4 - v3.pop()
            v2.add(v5)
            v8 = max(v8, v1 + len(v2) ** 2)
        return v8
