import collections

class C1(object):

    def numberOfSubsequences(self, a1):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = collections.defaultdict(int)
        v2 = 0
        for v3 in range(4, len(a1) - 2):
            v4 = v3 - 2
            for v5 in range(v4 - 2 + 1):
                v6 = gcd(a1[v5], a1[v4])
                v1[a1[v5] // v6, a1[v4] // v6] += 1
            for v7 in range(v3 + 2, len(a1)):
                v6 = gcd(a1[v7], a1[v3])
                v2 += v1[a1[v7] // v6, a1[v3] // v6]
        return v2
