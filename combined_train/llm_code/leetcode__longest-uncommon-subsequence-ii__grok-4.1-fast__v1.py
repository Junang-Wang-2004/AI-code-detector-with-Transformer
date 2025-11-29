class C1:

    def findLUSlength(self, a1):
        v1 = -1
        v2 = len(a1)
        for v3 in range(v2):
            v4 = a1[v3]
            v5 = len(v4)
            v6 = True
            for v7 in range(v2):
                if v3 == v7:
                    continue
                v8 = a1[v7]
                if len(v8) < v5:
                    continue
                v9 = 0
                for v10 in v8:
                    if v9 < v5 and v10 == v4[v9]:
                        v9 += 1
                if v9 == v5:
                    v6 = False
                    break
            if v6:
                v1 = max(v1, v5)
        return v1
