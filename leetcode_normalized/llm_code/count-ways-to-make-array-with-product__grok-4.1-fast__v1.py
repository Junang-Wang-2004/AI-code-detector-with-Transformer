class C1(object):

    def waysToFillArray(self, a1):
        v1 = 10 ** 9 + 7
        v2 = 100
        v3 = max((q[1] for v4 in a1))
        v5 = int(v3 ** 0.5) + 2

        def generate_primes(a1):
            if a1 < 2:
                return []
            v1 = [True] * (a1 + 1)
            v1[0] = v1[1] = False
            for v2 in range(2, int(a1 ** 0.5) + 1):
                if v1[v2]:
                    for v3 in range(v2 * v2, a1 + 1, v2):
                        v1[v3] = False
            return [v2 for v2 in range(2, a1 + 1) if v1[v2]]
        v6 = generate_primes(v5)

        def extract_exponents(a1, a2):
            v1 = []
            v2 = a1
            for v3 in a2:
                if v3 * v3 > v2:
                    break
                v4 = 0
                while v2 % v3 == 0:
                    v2 //= v3
                    v4 += 1
                if v4 > 0:
                    v1.append(v4)
            if v2 > 1:
                v1.append(1)
            return v1
        v7 = [1] * (v2 + 1)
        for v8 in range(1, v2 + 1):
            v7[v8] = v7[v8 - 1] * v8 % v1
        v9 = [pow(v7[i], v1 - 2, v1) for v10 in range(v2 + 1)]

        def repeated_combination(a1, a2, a3, a4):
            if a2 == 0:
                return 1
            v1 = 1
            for v2 in range(a2):
                v1 = v1 * ((a1 + v2) % a3) % a3
            return v1 * a4[a2] % a3
        v11 = []
        for v12 in a1:
            v13, v14 = v12
            v15 = extract_exponents(v14, v6)
            v16 = 1
            for v17 in v15:
                v16 = v16 * repeated_combination(v13, v17, v1, v9) % v1
            v11.append(v16)
        return v11
