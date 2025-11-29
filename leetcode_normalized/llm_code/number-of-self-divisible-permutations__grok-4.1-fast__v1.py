class C1(object):

    def selfDivisiblePermutationCount(self, a1):

        def compute_gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = [[j for v2 in range(a1) if compute_gcd(i + 1, v2 + 1) == 1] for v3 in range(a1)]
        v4 = 1 << a1
        v5 = [0] * v4
        v5[0] = 1
        for v6 in range(a1):
            v7 = [0] * v4
            for v8 in range(v4):
                if v5[v8]:
                    for v9 in v1[v6]:
                        if v8 & 1 << v9 == 0:
                            v7[v8 | 1 << v9] += v5[v8]
            v5 = v7
        return v5[v4 - 1]
