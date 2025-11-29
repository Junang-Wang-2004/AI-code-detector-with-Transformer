import bisect

class C1(object):

    def findMaximumLength(self, a1):
        """
        """
        v1 = [0] * (len(a1) + 1)
        for v2 in range(len(a1)):
            v1[v2 + 1] = v1[v2] + a1[v2]
        v3 = [float('inf')] * (len(a1) + 1)
        v3[0] = 0
        v4 = [-1] * (len(a1) + 1)
        v5 = -1
        for v6 in range(len(a1)):
            v5 = max(v5, v4[v6])
            v3[v6 + 1] = v3[v5 + 1] + 1
            v7 = bisect.bisect_left(v1, v1[v6 + 1] + (v1[v6 + 1] - v1[v5 + 1])) - 1
            v4[v7] = v6
        return v3[-1]
