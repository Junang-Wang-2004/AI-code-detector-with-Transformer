import collections

class C1(object):

    def waysToPartition(self, a1, a2):
        """
        """
        v1 = sum(a1)
        v2 = collections.Counter()
        v3 = 0
        for v4 in range(len(a1) - 1):
            v3 += a1[v4]
            v2[v3 - (v1 - v3)] += 1
        v5 = v2[0]
        v6 = collections.Counter()
        v3 = 0
        for v7 in a1:
            v5 = max(v5, v6[a2 - v7] + v2[-(a2 - v7)])
            v3 += v7
            v6[v3 - (v1 - v3)] += 1
            v2[v3 - (v1 - v3)] -= 1
        return v5
