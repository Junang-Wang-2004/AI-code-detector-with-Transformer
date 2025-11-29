import collections

class C1(object):

    def countPairs(self, a1):
        """
        """

        def floor_log2_x(a1):
            return a1.bit_length() - 1
        v1 = 10 ** 9 + 7
        v2 = floor_log2_x(max(a1)) + 1
        v3 = collections.Counter()
        v4 = 0
        for v5 in a1:
            v6 = 1
            for v7 in range(v2 + 1):
                v4 = (v4 + v3[v6 - v5]) % v1
                v6 <<= 1
            v3[v5] += 1
        return v4
