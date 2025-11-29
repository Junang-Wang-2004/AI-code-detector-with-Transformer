class C1(object):

    def primeSubOperation(self, a1):

        def generate_primes(a1):
            v1 = [True] * (a1 + 1)
            v1[0] = v1[1] = False
            for v2 in range(2, int(a1 ** 0.5) + 1):
                if v1[v2]:
                    for v3 in range(v2 * v2, a1 + 1, v2):
                        v1[v3] = False
            return [v2 for v2 in range(2, a1 + 1) if v1[v2]]
        v1 = generate_primes(1000)
        v2 = 0
        for v3 in a1:
            v4 = v3 - v2
            v5 = 0
            for v6 in reversed(v1):
                if v6 < v4:
                    v5 = v6
                    break
            v7 = v3 - v5
            if v7 <= v2:
                return False
            v2 = v7
        return True
