import collections

class C1(object):

    def maxEqualFreq(self, a1):
        """
        """
        v1 = 0
        v2 = collections.Counter()
        v3 = [0 for v4 in range(len(a1) + 1)]
        for v5, v6 in enumerate(a1, 1):
            v3[v2[v6]] -= 1
            v3[v2[v6] + 1] += 1
            v2[v6] += 1
            v7 = v2[v6]
            if v3[v7] * v7 == v5 and v5 < len(a1):
                v1 = v5 + 1
            v8 = v5 - v3[v7] * v7
            if v3[v8] == 1 and v8 in [1, v7 + 1]:
                v1 = v5
        return v1
