class C1:

    def minMovesToMakePalindrome(self, a1: str) -> int:
        v1 = len(a1)
        v2 = [[] for v3 in range(26)]
        for v4, v5 in enumerate(a1):
            v2[ord(v5) - ord('a')].append(v4)
        v6 = [-1] * v1
        v7 = []
        v8 = v1 // 2
        for v9 in v2:
            v10 = len(v9)
            for v11 in range(v10 // 2):
                v7.append((v9[v11], v9[v10 - 1 - v11]))
            if v10 % 2:
                v6[v9[v10 // 2]] = v8
        v7.sort(key=lambda x: x[0])
        v12 = len(v7)
        for v13 in range(v12):
            v14, v15 = v7[v13]
            v6[v14] = v13
            v6[v15] = v1 - 1 - v13
        v16 = [0] * (v1 + 2)

        def upd(a1, a2):
            a1 += 1
            while a1 <= v1:
                v16[a1] += a2
                a1 += a1 & -a1

        def pref(a1):
            a1 += 1
            v2 = 0
            while a1 > 0:
                v2 += v16[a1]
                a1 -= a1 & -a1
            return v2
        v17 = 0
        for v18 in v6:
            v17 += pref(v1 - 1) - pref(v18)
            upd(v18, 1)
        return v17
