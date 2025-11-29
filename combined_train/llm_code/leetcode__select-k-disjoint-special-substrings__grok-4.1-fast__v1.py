class C1:

    def maxSubstringLength(self, a1: str, a2: int) -> bool:
        v1 = len(a1)
        v2 = [-1] * 26
        v3 = [-1] * 26
        for v4 in range(v1):
            v5 = ord(a1[v4]) - ord('a')
            if v2[v5] == -1:
                v2[v5] = v4
            v3[v5] = v4
        v6 = []
        v7 = [v2[i] for v8 in range(26) if v2[v8] != -1]
        for v9 in v7:
            v5 = ord(a1[v9]) - ord('a')
            v10 = v3[v5]
            v11 = v9 + 1
            while v11 <= v10 and v2[ord(a1[v11]) - ord('a')] >= v9:
                v10 = max(v10, v3[ord(a1[v11]) - ord('a')])
                v11 += 1
            if v11 == v10 + 1 and (v9 != 0 or v10 != v1 - 1):
                v6.append((v9, v10))
        v6.sort(key=lambda interval: interval[1])
        v12 = 0
        v13 = float('-inf')
        for v14, v15 in v6:
            if v14 <= v13:
                v12 += 1
            else:
                v13 = v15
        v16 = len(v6) - v12
        return v16 >= a2
