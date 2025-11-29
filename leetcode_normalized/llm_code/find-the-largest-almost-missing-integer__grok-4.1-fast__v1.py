from collections import Counter

class C1(object):

    def largestInteger(self, a1, a2):
        """
        """
        v1 = len(a1)
        if a2 == v1:
            return max(a1)
        v2 = Counter(a1)
        if a2 == 1:
            return max((num for v3, v4 in v2.items() if v4 == 1), default=-1)
        v5 = -1
        v6 = a1[0]
        v7 = a1[-1]
        if v2[v6] == 1:
            v5 = max(v5, v6)
        if v2[v7] == 1:
            v5 = max(v5, v7)
        return v5
