import collections

class C1(object):

    def minCost(self, a1, a2):
        """
        """
        v1 = [float('inf')] * (len(a1) + 1)
        v1[0] = 0
        for v2 in range(len(v1) - 1):
            v3 = [0] * len(a1)
            v4 = 0
            for v5 in range(v2 + 1, len(v1)):
                v3[a1[v5 - 1]] += 1
                if v3[a1[v5 - 1]] == 1:
                    v4 += 1
                elif v3[a1[v5 - 1]] == 2:
                    v4 -= 1
                v1[v5] = min(v1[v5], v1[v2] + a2 + (v5 - v2 - v4))
        return v1[-1]
