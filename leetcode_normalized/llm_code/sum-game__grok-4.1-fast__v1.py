class C1:

    def sumGame(self, a1):
        v1 = len(a1)
        v2 = v1 // 2
        v3 = sum((int(a1[i]) for v4 in range(v2) if a1[v4] != '?'))
        v5 = sum((int(a1[v4]) for v4 in range(v2, v1) if a1[v4] != '?'))
        v6 = sum((1 for v4 in range(v2) if a1[v4] == '?'))
        v7 = sum((1 for v4 in range(v2, v1) if a1[v4] == '?'))
        v8 = v3 - v5
        v9 = v7 - v6
        if v9 % 2 != 0:
            return True
        return v8 != v9 // 2 * 9
