import collections

class C1(object):

    def minOperations(self, a1, a2):
        """
        """
        if len(a1) * 6 < len(a2) or len(a1) > len(a2) * 6:
            return -1
        v1 = sum(a2) - sum(a1)
        if v1 < 0:
            a1, a2 = (a2, a1)
            v1 = -v1
        v4 = collections.Counter((6 - num for v5 in a1))
        v4 += collections.Counter((v5 - 1 for v5 in a2))
        v6 = 0
        for v7 in reversed(range(1, 6)):
            if not v4[v7]:
                continue
            v8 = min(v4[v7], (v1 + v7 - 1) // v7)
            v6 += v8
            v1 -= v7 * v8
            if v1 <= 0:
                break
        return v6
