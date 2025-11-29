import collections

class C1(object):

    def meetRequirement(self, a1, a2, a3):
        """
        """
        v1 = collections.defaultdict(int)
        for v2, v3 in a2:
            v1[max(v2 - v3, 0)] += 1
            v1[min(v2 + v3, a1 - 1) + 1] -= 1
        v4 = v5 = 0
        for v6, v3 in enumerate(a3):
            v5 += v1.get(v6, 0)
            if v5 >= v3:
                v4 += 1
        return v4
