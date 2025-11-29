import collections

class C1(object):

    def minCharacters(self, a1, a2):
        """
        """
        v1 = collections.Counter((ord(c) - ord('a') for v2 in a1))
        v3 = collections.Counter((ord(v2) - ord('a') for v2 in a2))
        v4 = len(a1) + len(a2) - max((v1 + v3).values())
        for v5 in range(26 - 1):
            if v5 > 0:
                v1[v5] += v1[v5 - 1]
                v3[v5] += v3[v5 - 1]
            v4 = min(v4, len(a1) - v1[v5] + v3[v5])
            v4 = min(v4, len(a2) - v3[v5] + v1[v5])
        return v4
