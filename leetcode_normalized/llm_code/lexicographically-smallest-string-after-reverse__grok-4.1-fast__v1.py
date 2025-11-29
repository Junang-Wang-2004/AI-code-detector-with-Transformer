class C1:

    def lexSmallest(self, a1):
        v1 = len(a1)
        if v1 < 2:
            return a1
        v2 = 998244353
        v3 = 31
        v4 = [ord(c) for v5 in a1]
        v6 = [0] * (v1 + 1)
        for v7 in range(v1):
            v6[v7 + 1] = (v6[v7] * v3 + v4[v7]) % v2
        v8 = [0] * (v1 + 1)
        for v7 in range(v1 - 1, -1, -1):
            v8[v7] = (v8[v7 + 1] * v3 + v4[v7]) % v2
        v9 = [1] * (v1 + 1)
        for v7 in range(1, v1 + 1):
            v9[v7] = v9[v7 - 1] * v3 % v2

        def substr_fwd(a1, a2):
            if a1 > a2:
                return 0
            v1 = (v6[a2 + 1] - v6[a1] * v9[a2 - a1 + 1] % v2 + v2) % v2
            return v1

        def substr_rev(a1, a2):
            if a1 > a2:
                return 0
            v1 = (v8[a1] - v8[a2 + 1] * v9[a2 - a1 + 1] % v2 + v2) % v2
            return v1

        def prefix_hash(a1, a2):
            if a2 <= a1:
                return substr_rev(a1 - a2, a1 - 1)
            v1 = substr_rev(0, a1 - 1)
            v2 = substr_fwd(a1, a2 - 1)
            return (v1 * v9[a2 - a1] + v2) % v2

        def suffix_hash(a1, a2):
            v1 = v1 - a1
            if a2 <= v1:
                return substr_fwd(0, a2 - 1)
            v2 = substr_fwd(0, v1 - 1) if v1 else 0
            v3 = a2 - v1
            v4 = substr_rev(v1 - v3, v1 - 1)
            return (v2 * v9[v3] + v4) % v2

        def ch_at(a1, a2, a3):
            if not a2:
                return a1[a1 - 1 - a3] if a3 < a1 else a1[a3]
            v1 = v1 - a1
            return a1[a3] if a3 < v1 else a1[v1 - 1 - (a3 - v1)]

        def is_strictly_smaller(a1, a2, a3, a4):
            v1, v2 = (0, v1 - 1)
            while v1 <= v2:
                v3 = (v1 + v2) // 2
                v4 = suffix_hash(a1, v3 + 1) if a2 else prefix_hash(a1, v3 + 1)
                v5 = suffix_hash(a3, v3 + 1) if a4 else prefix_hash(a3, v3 + 1)
                if v4 == v5:
                    v1 = v3 + 1
                else:
                    v2 = v3 - 1
            v6 = v1
            if v6 == v1:
                return False
            return ch_at(a1, a2, v6) < ch_at(a3, a4, v6)
        v10 = min(a1)
        v11 = 1
        v12 = False
        for v13 in range(v1):
            if a1[v13] == v10:
                v14 = v13 + 1
                if is_strictly_smaller(v14, False, v11, v12):
                    v11 = v14
                    v12 = False
        for v14 in range(1, v1 + 1):
            if a1[v1 - v14] < a1[-1]:
                continue
            if is_strictly_smaller(v14, True, v11, v12):
                v11 = v14
                v12 = True
        if not v12:
            return a1[:v11][::-1] + a1[v11:]
        return a1[:-v11] + a1[-v11:][::-1]
