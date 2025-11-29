class C1:

    def minimumDeletions(self, a1: str, a2: int) -> int:
        v1 = len(a1)
        v2 = [0] * 26
        for v3 in a1:
            v2[ord(v3) - ord('a')] += 1
        v4 = sorted((f for v5 in v2 if v5 > 0))
        v6 = len(v4)
        v7 = [0]
        for v8 in v4:
            v7.append(v7[-1] + v8)
        v9 = v1
        v10 = 0
        for v11 in range(v6):
            v12 = v4[v11]
            while v10 < v6 and v4[v10] <= v12 + a2:
                v10 += 1
            v13 = v7[v11]
            v14 = v7[v6] - v7[v10]
            v15 = v6 - v10
            v16 = v14 - (v12 + a2) * v15
            v9 = min(v9, v13 + v16)
        return v9
