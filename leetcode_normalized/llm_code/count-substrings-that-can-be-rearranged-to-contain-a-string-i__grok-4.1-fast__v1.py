class C1:

    def validSubstringCount(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * 26
        for v3 in a2:
            v2[ord(v3) - ord('a')] += 1
        v4 = sum((v > 0 for v5 in v2))
        v6 = [0] * 26
        v7 = 0
        v8 = 0
        v9 = 0
        for v10 in range(v1):
            while v8 < v1 and v7 < v4:
                v11 = ord(a1[v8]) - ord('a')
                v12 = v6[v11]
                v6[v11] += 1
                if v2[v11] > 0 and v12 < v2[v11] <= v6[v11]:
                    v7 += 1
                v8 += 1
            if v7 == v4:
                v13 = max(v10, v8 - 1)
                v9 += v1 - v13
            v11 = ord(a1[v10]) - ord('a')
            v12 = v6[v11]
            v6[v11] -= 1
            if v2[v11] > 0 and v12 == v2[v11]:
                v7 -= 1
        return v9
