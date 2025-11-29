class C1:

    def shortestCommonSupersequence(self, a1, a2):
        v1, v2 = (len(a1), len(a2))
        v3 = [[0] * (v2 + 1) for v4 in range(v1 + 1)]
        for v5 in range(1, v1 + 1):
            for v6 in range(1, v2 + 1):
                if a1[v5 - 1] == a2[v6 - 1]:
                    v3[v5][v6] = v3[v5 - 1][v6 - 1] + 1
                else:
                    v3[v5][v6] = max(v3[v5 - 1][v6], v3[v5][v6 - 1])
        v7 = []
        v8, v9 = (v1, v2)
        while v8 or v9:
            if v8 and v9 and (a1[v8 - 1] == a2[v9 - 1]):
                v7.append(a1[v8 - 1])
                v8 -= 1
                v9 -= 1
            elif v8 and (not v9 or v3[v8][v9] == v3[v8 - 1][v9]):
                v7.append(a1[v8 - 1])
                v8 -= 1
            else:
                v7.append(a2[v9 - 1])
                v9 -= 1
        return ''.join(v7[::-1])
