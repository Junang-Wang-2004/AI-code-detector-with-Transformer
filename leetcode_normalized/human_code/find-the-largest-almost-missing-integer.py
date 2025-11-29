import collections

class C1(object):

    def largestInteger(self, a1, a2):
        """
        """
        if a2 == len(a1):
            return max(a1)
        v1 = collections.defaultdict(int)
        for v2 in a1:
            v1[v2] += 1
        if a2 == 1:
            return max((v2 for v2, v3 in v1.items() if v3 == 1)) if any((v == 1 for v3 in v1.values())) else -1
        v4 = -1
        if v1[a1[0]] == 1:
            v4 = max(v4, a1[0])
        if v1[a1[-1]] == 1:
            v4 = max(v4, a1[-1])
        return v4
