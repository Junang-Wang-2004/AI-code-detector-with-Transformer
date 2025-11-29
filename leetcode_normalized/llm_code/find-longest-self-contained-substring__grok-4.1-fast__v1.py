class C1:

    def maxSubstringLength(self, a1):
        v1 = len(a1)
        v2 = [v1] * 26
        v3 = [-1] * 26
        for v4, v5 in enumerate(a1):
            v6 = ord(v5) - ord('a')
            v2[v6] = min(v2[v6], v4)
            v3[v6] = max(v3[v6], v4)
        v7 = -1
        v8 = list(set((v2[k] for v9 in range(26) if v2[v9] < v1)))
        for v10 in v8:
            v11 = v1 + 5
            v12 = -5
            for v13 in range(v10, v1):
                v6 = ord(a1[v13]) - ord('a')
                v11 = min(v11, v2[v6])
                v12 = max(v12, v3[v6])
                if v11 >= v10 and v12 <= v13:
                    v14 = v13 - v10 + 1
                    if v14 < v1:
                        v7 = max(v7, v14)
                if v11 < v10:
                    break
        return v7
