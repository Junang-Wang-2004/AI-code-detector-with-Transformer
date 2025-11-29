import collections

class C1(object):

    def numTriplets(self, a1, a2):
        v1 = collections.Counter(a1)
        v2 = collections.Counter(a2)

        def get_pairs(a1, a2):
            v1 = 0
            for v2 in a1:
                if a2 % v2 != 0:
                    continue
                v3 = a2 // v2
                if v3 not in a1:
                    continue
                if v2 < v3:
                    v1 += a1[v2] * a1[v3]
                elif v2 == v3:
                    v1 += a1[v2] * (a1[v2] - 1) // 2
            return v1
        v3 = 0
        for v4 in a1:
            v3 += get_pairs(v2, v4 * v4)
        for v5 in a2:
            v3 += get_pairs(v1, v5 * v5)
        return v3
