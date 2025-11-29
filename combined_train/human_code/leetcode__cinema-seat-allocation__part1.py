import collections

class C1(object):

    def maxNumberOfFamilies(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(lambda: [False] * 3)
        for v2, v3 in a2:
            if 2 <= v3 <= 5:
                v1[v2][0] = True
            if 4 <= v3 <= 7:
                v1[v2][1] = True
            if 6 <= v3 <= 9:
                v1[v2][2] = True
        v4 = 2 * a1
        for v5, v6, v3 in v1.values():
            if not v5 and (not v3):
                continue
            if not v5 or not v6 or (not v3):
                v4 -= 1
                continue
            v4 -= 2
        return v4
