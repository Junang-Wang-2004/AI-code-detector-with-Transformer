import collections

class C1(object):

    def numberOfArithmeticSlices(self, a1):
        """
        """
        v1 = 0
        v2 = [collections.defaultdict(int) for v3 in range(len(a1))]
        for v3 in range(1, len(a1)):
            for v4 in range(v3):
                v5 = a1[v3] - a1[v4]
                v2[v3][v5] += 1
                if v5 in v2[v4]:
                    v2[v3][v5] += v2[v4][v5]
                    v1 += v2[v4][v5]
        return v1
