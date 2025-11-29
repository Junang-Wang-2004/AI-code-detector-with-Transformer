class C1:

    def minOperations(self, a1, a2, a3):
        v1 = v2 = 0
        v3 = len(a1)
        for v4 in range(v3):
            v5 = a1[v4]
            v6 = a2[v4]
            v7 = v6 - v5
            if v7 != 0:
                if a3 == 0 or v7 % a3 != 0:
                    return -1
                v8 = abs(v7) // a3
                if v7 > 0:
                    v1 += v8
                else:
                    v2 += v8
        return v1 if v1 == v2 else -1
