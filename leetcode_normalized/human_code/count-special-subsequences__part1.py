import collections

class C1(object):

    def numberOfSubsequences(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        v2 = 0
        for v3 in range(4, len(a1) - 2):
            v4 = v3 - 2
            for v5 in range(v4 - 2 + 1):
                v1[float(a1[v5]) / a1[v4]] += 1
            for v6 in range(v3 + 2, len(a1)):
                v2 += v1[float(a1[v6]) / a1[v3]]
        return v2
