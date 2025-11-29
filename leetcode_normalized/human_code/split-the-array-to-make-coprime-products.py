import collections

class C1(object):

    def findValidSplit(self, a1):
        """
        """

        def factorize(a1):
            v1 = []
            v2 = 2
            while v2 * v2 <= a1:
                v3 = 0
                while a1 % v2 == 0:
                    a1 //= v2
                    v3 += 1
                if v3:
                    v1.append([v2, v3])
                v2 += 1 if v2 == 2 else 2
            if a1 > 1:
                v1.append([a1, 1])
            return v1
        v1 = collections.Counter()
        for v2 in reversed(a1):
            for v3, v4 in factorize(v2):
                v1[v3] += v4
        v5 = collections.Counter()
        v6 = 0
        for v7 in range(len(a1) - 1):
            for v3, v4 in factorize(a1[v7]):
                if not v5[v3]:
                    v6 += 1
                v5[v3] += v4
                v1[v3] -= v4
                if not v1[v3]:
                    v6 -= 1
            if not v6:
                return v7
        return -1
