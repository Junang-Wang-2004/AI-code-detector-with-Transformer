class C1:

    def validSubstringCount(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * 26
        v3 = 0
        v4 = ord('a')
        for v5 in a2:
            v6 = ord(v5) - v4
            if v2[v6] == 0:
                v3 += 1
            v2[v6] += 1
        v7 = v2[:]
        v8 = v3
        v9 = 0
        v10 = 0
        for v11 in range(v1):
            v6 = ord(a1[v11]) - v4
            v7[v6] -= 1
            if v7[v6] == 0:
                v8 -= 1
            while v8 == 0:
                v9 += v1 - v11
                v12 = ord(a1[v10]) - v4
                if v7[v12] == 0:
                    v8 += 1
                v7[v12] += 1
                v10 += 1
        return v9
