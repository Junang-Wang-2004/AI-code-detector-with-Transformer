import collections
import heapq

class C1(object):

    def modeWeight(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(int)
        v2 = []
        v3 = 0
        for v4 in range(len(a1)):
            v1[a1[v4]] += 1
            heapq.heappush(v2, (-v1[a1[v4]], a1[v4]))
            if v4 >= a2 - 1:
                while -v2[0][0] != v1[v2[0][1]]:
                    heapq.heappop(v2)
                v3 += -v2[0][0] * v2[0][1]
                v1[a1[v4 - a2 + 1]] -= 1
        return v3
