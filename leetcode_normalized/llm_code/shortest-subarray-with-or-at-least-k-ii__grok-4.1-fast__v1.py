class C1:

    def minimumSubarrayLength(self, a1, a2):
        v1 = [0] * 32
        v2 = 0
        v3 = len(a1) + 1
        v4 = 0
        v5 = len(a1)
        for v6 in range(v5):
            v7 = a1[v6]
            for v8 in range(32):
                v9 = 1 << v8
                if v7 & v9:
                    if v1[v8] == 0:
                        v2 |= v9
                    v1[v8] += 1
            while v4 <= v6 and v2 >= a2:
                v3 = min(v3, v6 - v4 + 1)
                v10 = a1[v4]
                for v8 in range(32):
                    v9 = 1 << v8
                    if v10 & v9:
                        v1[v8] -= 1
                        if v1[v8] == 0:
                            v2 &= ~v9
                v4 += 1
        return v3 if v3 <= v5 else -1
