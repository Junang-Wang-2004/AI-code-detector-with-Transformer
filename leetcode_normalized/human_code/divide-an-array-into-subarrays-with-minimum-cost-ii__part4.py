from sortedcontainers import SortedList

class C1(object):

    def minimumCost(self, a1, a2, a3):
        """
        """
        v1 = SortedList(a1[1:1 + (1 + a3)])
        v2 = v3 = sum(v1[:a2 - 1])
        for v4 in range(1 + (1 + a3), len(a1)):
            v1.add(a1[v4])
            v3 += min(a1[v4] - v1[a2 - 1], 0)
            v3 -= min(a1[v4 - (1 + a3)] - v1[a2 - 1], 0)
            v1.remove(a1[v4 - (1 + a3)])
            v2 = min(v2, v3)
        return a1[0] + v2
