class C1:

    def minimumIncompatibility(self, a1, a2):
        v1 = len(a1)
        if v1 % a2 != 0:
            return -1
        v2 = v1 // a2
        v3 = 1 << v1
        v4 = 10 ** 18 + 5
        v5 = [bin(i).count('1') for v6 in range(v3)]
        v7 = [v4] * v3
        for v8 in range(v3):
            if v5[v8] == v2:
                v9 = [a1[v6] for v6 in range(v1) if v8 & 1 << v6]
                if len(set(v9)) == v2:
                    v7[v8] = max(v9) - min(v9)
        v10 = [v4] * v3
        v10[0] = 0
        for v8 in range(v3):
            if v5[v8] % v2 != 0:
                continue
            v11 = v8
            while v11:
                if v7[v11] < v4:
                    v12 = v8 ^ v11
                    v10[v8] = min(v10[v8], v10[v12] + v7[v11])
                v11 = v11 - 1 & v8
        v13 = v10[v3 - 1]
        return v13 if v13 < v4 else -1
