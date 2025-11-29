import collections

class C1(object):

    def subsequencePairCount(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v2 = max(a1)
        v3 = [[0] * (v2 + 1) for v4 in range(v2 + 1)]
        v3[0][0] = 1
        for v5 in a1:
            v6 = [row[:] for v7 in v3]
            for v8 in reversed(range(v2 + 1)):
                for v9 in reversed(range(v2 + 1)):
                    v10, v11 = (gcd(v8, v5), gcd(v9, v5))
                    v6[v10][v9] = (v6[v10][v9] + v3[v8][v9]) % v1
                    v6[v8][v11] = (v6[v8][v11] + v3[v8][v9]) % v1
            v3 = v6
        return reduce(lambda accu, x: (accu + v5) % v1, (v3[g][g] for v12 in range(1, v2 + 1)), 0)
