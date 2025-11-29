import collections

class C1(object):

    def countPairs(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = collections.defaultdict(collections.Counter)
        for v2, v3 in enumerate(a1):
            v1[v3][gcd(v2, a2)] += 1
        v4 = 0
        for v5 in v1.values():
            for v3 in v5.keys():
                for v6 in v5.keys():
                    if v3 > v6 or v3 * v6 % a2:
                        continue
                    v4 += v5[v3] * v5[v6] if v3 != v6 else v5[v3] * (v5[v3] - 1) // 2
        return v4
