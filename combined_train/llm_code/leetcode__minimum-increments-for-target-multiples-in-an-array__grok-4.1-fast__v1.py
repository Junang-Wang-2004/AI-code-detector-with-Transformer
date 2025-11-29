class C1:

    def minimumIncrements(self, a1, a2):
        v1 = float('inf')

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1

        def lcm(a1, a2):
            return a1 // gcd(a1, a2) * a2
        v2 = len(a2)
        v3 = 1 << v2
        v4 = [0] * v3
        for v5 in range(v3):
            v6 = 1
            for v7 in range(v2):
                if v5 & 1 << v7:
                    v6 = lcm(v6, a2[v7])
            v4[v5] = v6
        v8 = [v1] * v3
        v8[0] = 0
        for v6 in a1:
            v9 = v8[:]
            for v5 in range(v3):
                if v8[v5] == v1:
                    continue
                v10 = v3 - 1 ^ v5
                v11 = v10
                while v11:
                    v12 = v4[v11]
                    v13 = v6 % v12
                    v14 = 0 if v13 == 0 else v12 - v13
                    v15 = v5 | v11
                    v9[v15] = min(v9[v15], v8[v5] + v14)
                    v11 = v11 - 1 & v10
            v8 = v9
        return v8[v3 - 1]
