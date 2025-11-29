import collections

class C1(object):

    def minimumOperations(self, a1):
        """
        """
        v1 = collections.Counter((a1[i] for v2 in range(0, len(a1), 2))).most_common(2)
        v3 = collections.Counter((a1[v2] for v2 in range(1, len(a1), 2))).most_common(2)
        if not v3 or v1[0][0] != v3[0][0]:
            return len(a1) - v1[0][1] - (v3[0][1] if v3 else 0)
        return min(len(a1) - v1[0][1] - (v3[1][1] if len(v3) == 2 else 0), len(a1) - v3[0][1] - (v1[1][1] if len(v1) == 2 else 0))
