class C1(object):

    def subsequenceSumAfterCapping(self, a1, a2):
        v1 = len(a1)
        v2 = [False] * v1
        a1.sort()
        v3 = [False] * (a2 + 1)
        v3[0] = True
        v4 = 0
        for v5 in range(1, v1 + 1):
            while v4 < v1 and a1[v4] < v5:
                v6 = a1[v4]
                v7 = v3[:]
                for v8 in range(a2 - v6 + 1):
                    if v3[v8]:
                        v7[v8 + v6] = True
                v3 = v7
                v4 += 1
            v9 = v1 - v4
            v10 = a2 % v5
            v11 = max(v10, a2 - v9 * v5)
            v12 = False
            v13 = v11
            while v13 <= a2:
                if v3[v13]:
                    v12 = True
                    break
                v13 += v5
            v2[v5 - 1] = v12
        return v2
