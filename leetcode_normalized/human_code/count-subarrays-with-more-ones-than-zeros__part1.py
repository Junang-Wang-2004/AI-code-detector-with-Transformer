import collections

class C1(object):

    def subarraysWithMoreZerosThanOnes(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = collections.defaultdict(int)
        v2[0] = 1
        v3 = v4 = v5 = v6 = 0
        for v7 in a1:
            v4 += 1 if v7 == 1 else -1
            v8 = v2[v4]
            v9 = (v5 + v6 + 1) % v1 if v7 == 1 else (v6 - v8) % v1
            v2[v4] += 1
            v3 = (v3 + v9) % v1
            v5, v6 = (v8, v9)
        return v3
