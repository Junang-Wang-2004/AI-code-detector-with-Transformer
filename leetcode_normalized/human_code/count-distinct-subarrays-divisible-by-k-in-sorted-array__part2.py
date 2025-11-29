import collections

class C1(object):

    def numGoodSubarrays(self, a1, a2):
        """
        """
        v1 = v2 = 0
        v3 = collections.defaultdict(int)
        v3[0] = 1
        for v4 in a1:
            v2 = (v2 + v4) % a2
            v1 += v3[v2]
            v3[v2] += 1
        v5 = 0
        for v6 in range(len(a1)):
            v5 += 1
            if v6 + 1 == len(a1) or a1[v6 + 1] != a1[v6]:
                for v7 in range(1, v5 + 1):
                    if a1[v6] * v7 % a2 == 0:
                        v1 -= v5 - v7 + 1 - 1
                v5 = 0
        return v1
