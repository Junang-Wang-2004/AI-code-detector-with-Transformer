import collections

class C1(object):

    def countPairs(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = collections.Counter()
        for v2 in a1:
            v1[gcd(v2, a2)] += 1
        v3 = 0
        for v2 in v1.keys():
            for v4 in v1.keys():
                if v2 > v4 or v2 * v4 % a2:
                    continue
                v3 += v1[v2] * v1[v4] if v2 != v4 else v1[v2] * (v1[v2] - 1) // 2
        return v3
