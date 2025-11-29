import collections

class C1(object):

    def countPairs(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = collections.defaultdict(list)
        for v2, v3 in enumerate(a1):
            v1[v3].append(v2)
        v4 = 0
        for v5 in v1.values():
            v6 = collections.Counter()
            for v2 in v5:
                v7 = gcd(v2, a2)
                v4 += sum((cnt for v8, v9 in v6.items() if v7 * v8 % a2 == 0))
                v6[v7] += 1
        return v4
