import collections

class C1(object):

    def minimumTotalDistance(self, a1, a2):
        """
        """
        (a1.sort(), a2.sort())
        v1 = [float('inf')] * (len(a1) + 1)
        v1[0] = 0
        for v2 in range(len(a2)):
            for v3 in reversed(range(1, len(a1) + 1)):
                v4 = 0
                for v5 in range(min(a2[v2][1], v3) + 1):
                    v1[v3] = min(v1[v3], v1[v3 - v5] + v4)
                    if v3 - 1 - v5 >= 0:
                        v4 += abs(a1[v3 - 1 - v5] - a2[v2][0])
        return v1[-1]
