class C1:

    def findAllConcatenatedWordsInADict(self, a1):
        v1 = set(a1)
        v2 = []
        for v3 in a1:
            v4 = v1 - {v3}
            v5 = len(v3)
            v6 = [False] * (v5 + 1)
            v6[0] = True
            for v7 in range(1, v5 + 1):
                for v8 in range(1, v7 + 1):
                    v9 = v7 - v8
                    if v6[v9] and v3[v9:v7] in v4:
                        v6[v7] = True
                        break
            if v6[v5]:
                v2.append(v3)
        return v2
