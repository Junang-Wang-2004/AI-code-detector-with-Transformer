class C1:

    def lexSmallest(self, a1):
        v1 = len(a1)
        v2 = 10 ** 9 + 7
        v3 = 31
        v4 = [1] * (v1 + 1)
        for v5 in range(1, v1 + 1):
            v4[v5] = v4[v5 - 1] * v3 % v2
        v6 = [0] * (v1 + 1)
        for v5 in range(v1):
            v6[v5 + 1] = (v6[v5] * v3 + ord(a1[v5])) % v2
        v7 = [0] * (v1 + 1)
        for v5 in range(v1 - 1, -1, -1):
            v7[v5] = (v7[v5 + 1] * v3 + ord(a1[v5])) % v2

        def substr_fwd(a1, a2):
            if a1 > a2:
                return 0
            v1 = a2 - a1 + 1
            return (v6[a2 + 1] - v6[a1] * v4[v1] % v2 + v2) % v2

        def substr_rev(a1, a2):
            if a1 > a2:
                return 0
            v1 = a2 - a1 + 1
            return (v7[a1] - v7[a2 + 1] * v4[v1] % v2 + v2) % v2

        def trans_hash(a1, a2, a3):
            if a3 == 0:
                return 0
            if not a2:
                if a3 <= a1:
                    return substr_rev(a1 - a3, a1 - 1)
                v1 = a3 - a1
                v2 = substr_rev(0, a1 - 1)
                v3 = substr_fwd(a1, a1 + v1 - 1)
                return (v2 * v4[v1] % v2 + v3) % v2
            else:
                v4 = v1 - a1
                if a3 <= v4:
                    return substr_fwd(0, a3 - 1)
                v1 = a3 - v4
                v2 = substr_fwd(0, v4 - 1)
                v3 = substr_rev(v1 - v1, v1 - 1)
                return (v2 * v4[v1] % v2 + v3) % v2

        def char_at(a1, a2, a3):
            if not a2:
                return a1[a1 - 1 - a3] if a3 < a1 else a1[a3]
            v1 = v1 - a1
            return a1[a3] if a3 < v1 else a1[v1 - 1 - (a3 - v1)]

        def first_diff(a1, a2, a3, a4):
            v1, v2 = (0, v1)
            while v1 < v2:
                v3 = (v1 + v2) // 2
                if trans_hash(a1, a2, v3 + 1) != trans_hash(a3, a4, v3 + 1):
                    v2 = v3
                else:
                    v1 = v3 + 1
            return v1

        def better(a1, a2, a3, a4):
            v1 = first_diff(a1, a2, a3, a4)
            if v1 == v1:
                return False
            return char_at(a1, a2, v1) < char_at(a3, a4, v1)
        v8 = min(a1)
        v9, v10 = (1, False)
        for v11 in range(v1):
            if a1[v11] == v8:
                v12 = v11 + 1
                if better(v12, False, v9, v10):
                    v9, v10 = (v12, False)
        for v12 in range(1, v1 + 1):
            if a1[v1 - v12] < a1[v1 - 1]:
                continue
            if better(v12, True, v9, v10):
                v9, v10 = (v12, True)
        if not v10:
            return a1[:v9][::-1] + a1[v9:]
        return a1[:v1 - v9] + a1[v1 - v9:][::-1]
