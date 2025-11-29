import math

class C1:

    def idealArrays(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = a2
        v3 = a1 + 30
        v4 = [1] * (v3 + 1)
        for v5 in range(1, v3 + 1):
            v4[v5] = v4[v5 - 1] * v5 % v1
        v6 = [0] * (v3 + 1)
        v6[v3] = pow(v4[v3], v1 - 2, v1)
        for v5 in range(v3 - 1, -1, -1):
            v6[v5] = v6[v5 + 1] * (v5 + 1) % v1

        def binomial(a1, a2):
            if a2 < 0 or a2 > a1:
                return 0
            return v4[a1] * v6[a2] % v1 * v6[a1 - a2] % v1
        v7 = int(math.sqrt(v2)) + 1
        v8 = [True] * (v7 + 1)
        v8[0] = v8[1] = False
        v9 = []
        for v5 in range(2, v7 + 1):
            if v8[v5]:
                v9.append(v5)
                for v10 in range(v5 * v5, v7 + 1, v5):
                    v8[v10] = False

        def get_exponents(a1):
            v1 = {}
            for v2 in v9:
                if v2 * v2 > a1:
                    break
                v3 = 0
                while a1 % v2 == 0:
                    v3 += 1
                    a1 //= v2
                if v3:
                    v1[v2] = v3
            if a1 > 1:
                v1[a1] = 1
            return v1
        v11 = 0
        for v12 in range(1, v2 + 1):
            v13 = get_exponents(v12)
            v14 = 1
            for v15 in v13.values():
                v14 = v14 * binomial(a1 + v15 - 1, v15) % v1
            v11 = (v11 + v14) % v1
        return v11
