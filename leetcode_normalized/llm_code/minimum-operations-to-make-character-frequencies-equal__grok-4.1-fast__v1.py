class C1(object):

    def makeStringGood(self, a1):
        v1 = len(a1)
        v2 = [0] * 26
        for v3 in a1:
            v2[ord(v3) - ord('a')] += 1
        v4 = v1
        v5 = [f for v6 in v2 if v6 > 0]
        if not v5:
            return v4
        v7 = min(v5)
        v8 = max(v2)
        v9 = v1 + 1
        for v10 in range(v7, v8 + 1):
            v11 = [[v9] * 2 for v12 in range(27)]
            v11[0][0] = v11[0][1] = 0
            for v13 in range(1, 27):
                v14 = v13 - 1
                v15 = v2[v14]
                v16 = 0
                if v14 > 0:
                    v17 = v2[v14 - 1]
                    v16 = v17 - v10 if v17 >= v10 else v17
                v18 = v11[v13 - 1][0]
                v19 = v11[v13 - 1][1]
                v20 = min(v18, v19)
                if v15 == 0:
                    v11[v13][0] = v18
                    v11[v13][1] = v19
                    continue
                if v15 >= v10:
                    v11[v13][0] = v9
                    v11[v13][1] = v20 + v15 - v10
                else:
                    v21 = v10 - v15
                    v22 = min(v20 + v21, v19 + max(0, v21 - v16))
                    v23 = v20 + v15
                    v11[v13][0] = v22
                    v11[v13][1] = v23
            v24 = min(v11[26][0], v11[26][1])
            v4 = min(v4, v24)
        return v4
