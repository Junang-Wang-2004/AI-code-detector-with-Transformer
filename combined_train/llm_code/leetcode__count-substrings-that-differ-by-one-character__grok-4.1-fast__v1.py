class C1(object):

    def countSubstrings(self, a1, a2):

        def diag(a1, a2):
            v1 = len(a1) - a1
            v2 = len(a2) - a2
            v3 = min(v1, v2)
            v4 = []
            for v5 in range(v3):
                if a1[a1 + v5] != a2[a2 + v5]:
                    v4.append(v5)
            v6 = 0
            v7 = -1
            v8 = len(v4)
            for v9 in range(v8):
                v10 = v4[v9]
                v11 = v10 - v7
                v12 = v3 if v9 + 1 == v8 else v4[v9 + 1]
                v13 = v12 - v10
                v6 += v11 * v13
                v7 = v10
            return v6
        v1 = 0
        v2 = len(a1)
        for v3 in range(v2):
            v1 += diag(v3, 0)
        v4 = len(a2)
        for v5 in range(1, v4):
            v1 += diag(0, v5)
        return v1
