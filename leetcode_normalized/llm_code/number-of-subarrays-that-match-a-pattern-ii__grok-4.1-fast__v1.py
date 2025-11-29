class C1:

    def countMatchingSubarrays(self, a1, a2):
        v1 = len(a1) - 1
        v2 = len(a2)
        if v1 < v2:
            return 0
        v3 = [0] * v1
        for v4 in range(v1):
            v5 = a1[v4 + 1] - a1[v4]
            v3[v4] = 1 if v5 > 0 else -1 if v5 < 0 else 0
        v6 = [0] * v2
        v7 = 0
        v8 = 1
        while v8 < v2:
            if a2[v8] == a2[v7]:
                v7 += 1
                v6[v8] = v7
                v8 += 1
            elif v7 != 0:
                v7 = v6[v7 - 1]
            else:
                v6[v8] = 0
                v8 += 1
        v9 = 0
        v10 = 0
        v11 = 0
        while v11 < v1:
            while v10 > 0 and v3[v11] != a2[v10]:
                v10 = v6[v10 - 1]
            if v3[v11] == a2[v10]:
                v10 += 1
            if v10 == v2:
                v9 += 1
                v10 = v6[v10 - 1]
            v11 += 1
        return v9
