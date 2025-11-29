import collections

class C1(object):

    def countQuadruplets(self, a1):
        """
        """
        v1 = 0
        v2 = collections.defaultdict(int)
        v2[a1[-1]] = 1
        for v3 in reversed(range(2, len(a1) - 1)):
            for v4 in range(1, v3):
                for v5 in range(v4):
                    if a1[v5] + a1[v4] + a1[v3] in v2:
                        v1 += v2[a1[v5] + a1[v4] + a1[v3]]
            v2[a1[v3]] += 1
        return v1
