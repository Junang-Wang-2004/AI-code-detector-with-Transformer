import sys
sys.setrecursionlimit(10 ** 6)

class C1:

    def numOfWays(self, a1):
        v1 = 10 ** 9 + 7
        v2 = 1005
        v3 = [1] * v2
        for v4 in range(1, v2):
            v3[v4] = v3[v4 - 1] * v4 % v1

        def mod_inverse(a1):
            return pow(a1, v1 - 2, v1)

        def binomial(a1, a2):
            if a2 < 0 or a2 > a1:
                return 0
            return v3[a1] * mod_inverse(v3[a2]) % v1 * mod_inverse(v3[a1 - a2]) % v1

        def compute_ways(a1):
            v1 = len(a1)
            if v1 <= 2:
                return 1
            v2 = a1[0]
            v3 = []
            v4 = []
            for v5 in a1[1:]:
                if v5 < v2:
                    v3.append(v5)
                else:
                    v4.append(v5)
            v6 = binomial(v1 - 1, len(v3))
            v7 = compute_ways(v3)
            v8 = compute_ways(v4)
            return v6 * v7 % v1 * v8 % v1
        v5 = compute_ways(a1)
        return (v5 - 1) % v1
