import collections

class C1(object):

    def specialTriplets(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = 0
        v3 = [collections.defaultdict(int) for v4 in range(2)]
        for v5 in a1:
            if v5 % 2 == 0 and v5 // 2 in v3[1]:
                v2 = (v2 + v3[1][v5 // 2]) % v1
            if 2 * v5 in v3[0]:
                v3[1][v5] = (v3[1][v5] + v3[0][2 * v5]) % v1
            v3[0][v5] = (v3[0][v5] + 1) % v1
        return v2
