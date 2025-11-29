import collections
import bisect

class C1(object):

    def gcdValues(self, a1, a2):
        """
        """
        v1 = collections.Counter(a1)
        v2 = [0] * (max(a1) + 1)
        for v3 in reversed(range(1, len(v2))):
            v4 = sum((v1[ng] for v5 in range(v3, len(v2), v3)))
            v2[v3] = v4 * (v4 - 1) // 2 - sum((v2[v5] for v5 in range(v3 + v3, len(v2), v3)))
        v6 = [0] * (len(v2) + 1)
        for v7 in range(len(v6) - 1):
            v6[v7 + 1] = v6[v7] + v2[v7]
        return [bisect.bisect_right(v6, q) - 1 for v8 in a2]
