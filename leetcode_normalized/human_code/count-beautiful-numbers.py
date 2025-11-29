import collections

class C1(object):

    def beautifulNumbers(self, a1, a2):
        """
        """

        def count(a1):
            v1 = [ord(a1) - ord('0') for a1 in str(a1)]
            v2 = [collections.defaultdict(int) for v3 in range(2)]
            v2[1][1, 0] = 1
            for v4 in v1:
                v5 = [collections.defaultdict(int) for v3 in range(2)]
                for v6 in range(2):
                    for (v7, v8), v9 in v2[v6].items():
                        for a1 in range((v4 if v6 else 9) + 1):
                            v5[v6 and a1 == v4][v7 * (1 if v8 == 0 == a1 else a1), v8 + a1] += v9
                v2 = v5
            v11 = 0
            for v6 in range(2):
                for (v7, v8), v9 in v2[v6].items():
                    if v8 and v7 % v8 == 0:
                        v11 += v9
            return v11
        return count(a2) - count(a1 - 1)
