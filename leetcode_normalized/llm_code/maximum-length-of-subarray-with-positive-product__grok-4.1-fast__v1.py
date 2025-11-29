class C1:

    def getMaxLen(self, a1):
        v1 = 0
        v2 = 0
        v3 = len(a1)
        while v2 < v3:
            if a1[v2] == 0:
                v2 += 1
                continue
            v4 = v2
            while v4 < v3 and a1[v4] != 0:
                v4 += 1
            v4 -= 1
            v5 = 0
            v6 = -1
            for v7 in range(v2, v4 + 1):
                if a1[v7] < 0:
                    v5 += 1
                    if v6 == -1:
                        v6 = v7
            v8 = v4 - v2 + 1
            if v5 % 2 == 0:
                v1 = max(v1, v8)
            elif v6 != -1:
                v1 = max(v1, v4 - v6)
            v2 = v4 + 1
        return v1
