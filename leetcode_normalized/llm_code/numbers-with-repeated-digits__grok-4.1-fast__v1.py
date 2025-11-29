class C1:

    def numDupDigitsAtMostN(self, a1):
        v1 = str(a1 + 1)
        v2 = [int(c) for v3 in v1]
        v4 = len(v2)

        def perms(a1, a2):
            v1 = 1
            for v2 in range(a2):
                v1 *= a1 - v2
            return v1
        v5 = 0
        for v6 in range(1, v4):
            v5 += 9 * perms(9, v6 - 1)
        v7 = set()
        for v8 in range(v4):
            v9 = v2[v8]
            v10 = 1 if v8 == 0 else 0
            for v11 in range(v10, v9):
                if v11 in v7:
                    continue
                v12 = v4 - v8 - 1
                v13 = 10 - len(v7) - 1
                v5 += perms(v13, v12)
            if v9 in v7:
                break
            v7.add(v9)
        return a1 - v5
