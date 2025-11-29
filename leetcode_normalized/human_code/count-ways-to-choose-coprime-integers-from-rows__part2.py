import collections

class C1(object):

    def countCoprime(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v2 = collections.defaultdict(int)
        v2[0] = 1
        for v3 in a1:
            v4 = collections.defaultdict(int)
            for v5 in v3:
                for v6, v7 in v2.items():
                    v8 = gcd(v6, v5)
                    v4[v8] = (v4[v8] + v7) % v1
            v2 = v4
        return v2[1]
