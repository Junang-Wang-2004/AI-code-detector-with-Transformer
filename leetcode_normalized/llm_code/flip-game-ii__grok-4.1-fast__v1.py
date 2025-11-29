class C1:

    def canWin(self, a1: str) -> bool:
        v1 = len(a1)
        v2 = []
        v3 = 0
        while v3 < v1:
            if a1[v3] == '+':
                v4 = v3
                while v3 < v1 and a1[v3] == '+':
                    v3 += 1
                v2.append(v3 - v4)
            else:
                v3 += 1
        if not v2:
            return False
        v5 = max(v2)
        v6 = [0] * (v5 + 1)
        for v7 in range(2, v5 + 1):
            v8 = set()
            for v9 in range(v7 - 1):
                v10 = v7 - v9 - 2
                v8.add(v6[v9] ^ v6[v10])
            v11 = 0
            while v11 in v8:
                v11 += 1
            v6[v7] = v11
        v12 = 0
        for v13 in v2:
            v12 ^= v6[v13]
        return v12 != 0
