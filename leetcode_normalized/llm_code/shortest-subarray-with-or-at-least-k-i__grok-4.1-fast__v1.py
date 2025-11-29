class C1:

    def minimumSubarrayLength(self, a1, a2):
        v1 = 0
        for v2 in a1:
            v1 |= v2
        if v1 < a2:
            return -1
        v3 = [0] * 32
        v4 = 0
        v5 = len(a1) + 1
        v6 = 0
        for v7 in range(len(a1)):
            v8 = a1[v7]
            for v9 in range(32):
                if 1 << v9 & v8:
                    v3[v9] += 1
                    if v3[v9] == 1:
                        v4 |= 1 << v9
            while v6 <= v7 and v4 >= a2:
                v5 = min(v5, v7 - v6 + 1)
                v10 = a1[v6]
                for v9 in range(32):
                    if 1 << v9 & v10:
                        v3[v9] -= 1
                        if v3[v9] == 0:
                            v4 &= ~(1 << v9)
                v6 += 1
        return v5 if v5 <= len(a1) else -1
