import collections

class C1(object):

    def countPairs(self, a1, a2):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = 0
        v2 = collections.Counter()
        for v3 in a1:
            v4 = gcd(v3, a2)
            v1 += sum((cnt for v5, v6 in v2.items() if v4 * v5 % a2 == 0))
            v2[v4] += 1
        return v1
