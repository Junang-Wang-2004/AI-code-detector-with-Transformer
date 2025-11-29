import collections

class C1(object):

    def findShortestSubArray(self, a1):
        """
        """
        v1 = collections.Counter(a1)
        v2, v3 = ({}, {})
        for v4, v5 in enumerate(a1):
            v2.setdefault(v5, v4)
            v3[v5] = v4
        v6 = max(v1.values())
        return min((v3[v5] - v2[v5] + 1 for v5 in list(v1.keys()) if v1[v5] == v6))
