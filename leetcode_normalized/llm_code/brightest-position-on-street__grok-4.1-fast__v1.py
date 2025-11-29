class C1:

    def brightestPosition(self, a1):
        v1 = []
        for v2, v3 in a1:
            v1.append((v2 - v3, 1))
            v1.append((v2 + v3 + 1, -1))
        v1.sort()
        v4 = 0
        v5 = 0
        v6 = None
        v7 = 0
        v8 = len(v1)
        while v7 < v8:
            v9 = v1[v7][0]
            v10 = 0
            while v7 < v8 and v1[v7][0] == v9:
                v10 += v1[v7][1]
                v7 += 1
            v5 += v10
            if v5 > v4:
                v4 = v5
                v6 = v9
        return v6
