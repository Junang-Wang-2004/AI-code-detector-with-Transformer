class C1:

    def longestBalanced(self, a1):
        v1 = 0
        v2 = len(a1)
        if v2 == 0:
            return 0
        v3 = 1
        for v4 in range(1, v2):
            if a1[v4] == a1[v4 - 1]:
                v3 += 1
            else:
                v1 = max(v1, v3)
                v3 = 1
        v1 = max(v1, v3)
        v5 = [('a', 'b'), ('b', 'c'), ('c', 'a')]
        for v6, v7 in v5:
            v8 = {0: -1}
            v9 = 0
            for v4 in range(v2):
                v10 = a1[v4]
                if v10 == v6:
                    v9 += 1
                elif v10 == v7:
                    v9 -= 1
                else:
                    v8 = {0: v4}
                    v9 = 0
                    continue
                if v9 in v8:
                    v1 = max(v1, v4 - v8[v9])
                else:
                    v8[v9] = v4
        v11 = {(0, 0): -1}
        v12 = v13 = 0
        for v4 in range(v2):
            if a1[v4] == 'a':
                v12 += 1
            elif a1[v4] == 'b':
                v13 += 1
            else:
                v12 -= 1
                v13 -= 1
            v14 = (v12, v13)
            if v14 in v11:
                v1 = max(v1, v4 - v11[v14])
            else:
                v11[v14] = v4
        return v1
