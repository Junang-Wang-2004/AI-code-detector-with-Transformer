class C1:

    def minimumDeleteSum(self, a1, a2):
        v1, v2 = (len(a1), len(a2))
        v3 = sum((ord(c) for v4 in a1 + a2))
        v5 = [0] * (v2 + 1)
        for v6 in range(v1):
            v7 = [0] * (v2 + 1)
            for v8 in range(v2):
                if a1[v6] == a2[v8]:
                    v7[v8 + 1] = v5[v8] + ord(a1[v6])
                else:
                    v7[v8 + 1] = max(v5[v8 + 1], v7[v8])
            v5 = v7
        return v3 - 2 * v5[v2]
