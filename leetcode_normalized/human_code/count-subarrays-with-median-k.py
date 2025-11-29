import collections

class C1(object):

    def countSubarrays(self, a1, a2):
        """
        """
        v1 = a1.index(a2)
        v2 = collections.Counter()
        v3 = 0
        for v4 in reversed(range(v1 + 1)):
            v3 += 0 if a1[v4] == a2 else -1 if a1[v4] < a2 else +1
            v2[v3] += 1
        v5 = v3 = 0
        for v4 in range(v1, len(a1)):
            v3 += 0 if a1[v4] == a2 else -1 if a1[v4] < a2 else +1
            v5 += v2[-v3] + v2[-(v3 - 1)]
        return v5
