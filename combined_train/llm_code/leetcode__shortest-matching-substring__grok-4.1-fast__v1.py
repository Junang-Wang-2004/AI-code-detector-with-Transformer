class C1:

    def shortestMatchingSubstring(self, a1, a2):
        v1 = a2.split('*')
        v2, v3, v4 = v1
        v5 = len(v2)
        v6 = len(v3)
        v7 = len(v4)
        v8 = len(a1)

        def compute_lps(a1):
            v1 = len(a1)
            v2 = [0] * v1
            v3 = 0
            v4 = 1
            while v4 < v1:
                if a1[v4] == a1[v3]:
                    v3 += 1
                    v2[v4] = v3
                    v4 += 1
                elif v3 != 0:
                    v3 = v2[v3 - 1]
                else:
                    v2[v4] = 0
                    v4 += 1
            return v2

        def get_match_starts(a1, a2):
            v1 = len(a1)
            if len(a2) == 0:
                return list(range(v1 + 1))
            v2 = compute_lps(a2)
            v3 = []
            v4 = 0
            for v5 in range(v1):
                while v4 > 0 and a2[v4] != a1[v5]:
                    v4 = v2[v4 - 1]
                if a2[v4] == a1[v5]:
                    v4 += 1
                if v4 == len(a2):
                    v3.append(v5 - len(a2) + 1)
                    v4 = v2[v4 - 1]
            return v3
        v9 = get_match_starts(a1, v2)
        v10 = get_match_starts(a1, v3)
        v11 = get_match_starts(a1, v4)
        v12 = float('inf')
        v13 = 0
        v14 = 0
        v15 = len(v9)
        v16 = len(v10)
        v17 = len(v11)
        for v18 in range(v15):
            v19 = v9[v18]
            v20 = v19 + v5
            while v13 < v16 and v10[v13] < v20:
                v13 += 1
            if v13 >= v16:
                break
            v21 = v10[v13]
            v22 = v21 + v6
            while v14 < v17 and v11[v14] < v22:
                v14 += 1
            if v14 >= v17:
                break
            v23 = v11[v14]
            v24 = v23 + v7 - 1
            v25 = v24 - v19 + 1
            if v25 < v12:
                v12 = v25
        return v12 if v12 != float('inf') else -1
