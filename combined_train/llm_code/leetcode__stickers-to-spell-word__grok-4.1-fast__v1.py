class C1:

    def minStickers(self, a1, a2):
        v1 = len(a2)
        v2 = ord('a')
        v3 = []
        for v4 in a1:
            v5 = [0] * 26
            for v6 in v4:
                v5[ord(v6) - v2] += 1
            v3.append(v5)
        v7 = [-1] * (1 << v1)

        def dfs(a1):
            if a1 == 0:
                return 0
            if v7[a1] != -1:
                return v7[a1]
            v1 = 999
            for v2 in v3:
                v3 = v2[:]
                v4 = 0
                for v5 in range(v1):
                    if a1 & 1 << v5 != 0:
                        v6 = ord(a2[v5]) - v2
                        if v3[v6] > 0:
                            v3[v6] -= 1
                            v4 |= 1 << v5
                if v4 != 0:
                    v7 = dfs(a1 & ~v4)
                    if v7 != -1:
                        v1 = min(v1, v7 + 1)
            v7[a1] = -1 if v1 == 999 else v1
            return v7[a1]
        v8 = (1 << v1) - 1
        return dfs(v8)
