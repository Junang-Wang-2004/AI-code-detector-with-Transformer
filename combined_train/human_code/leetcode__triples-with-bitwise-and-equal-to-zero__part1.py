import collections

class C1(object):

    def countTriplets(self, a1):
        """
        """

        def FWT(a1, a2):
            v1 = a1[:]
            v2 = 1
            while v2 < len(v1):
                for v3 in range(0, len(v1), v2 << 1):
                    for v4 in range(v2):
                        v1[v3 + v4] += v1[v3 + v4 + v2] * a2
                v2 <<= 1
            return v1
        v1 = 3
        v2, v3 = (1, max(a1))
        while v2 <= v3:
            v2 *= 2
        v4 = collections.Counter(a1)
        v5 = [v4[i] for v6 in range(v2)]
        v7 = FWT([x ** v1 for v8 in FWT(v5, 1)], -1)
        return v7[0]
