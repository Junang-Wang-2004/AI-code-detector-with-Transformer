class C1:

    def getWordsInLongestSubsequence(self, a1, a2, a3):
        v1 = [1] * a1
        v2 = [-1] * a1
        for v3 in range(a1 - 1, -1, -1):
            for v4 in range(v3 + 1, a1):
                if a3[v3] != a3[v4] and len(a2[v3]) == len(a2[v4]):
                    v5 = 0
                    for v6, v7 in zip(a2[v3], a2[v4]):
                        if v6 != v7:
                            v5 += 1
                            if v5 > 1:
                                break
                    if v5 == 1 and v1[v4] + 1 > v1[v3]:
                        v1[v3] = v1[v4] + 1
                        v2[v3] = v4
        v8 = 0
        for v9 in range(1, a1):
            if v1[v9] > v1[v8]:
                v8 = v9
        v10 = []
        v11 = v8
        while v11 != -1:
            v10.append(a2[v11])
            v11 = v2[v11]
        return v10
