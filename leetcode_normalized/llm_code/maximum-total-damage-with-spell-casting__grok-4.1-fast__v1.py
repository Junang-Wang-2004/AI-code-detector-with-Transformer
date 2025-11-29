class C1:

    def maximumTotalDamage(self, a1):
        a1.sort()
        if not a1:
            return 0
        v1 = []
        v2 = 0
        v3 = len(a1)
        while v2 < v3:
            v4 = a1[v2]
            v5 = 0
            while v2 < v3 and a1[v2] == v4:
                v5 += a1[v2]
                v2 += 1
            v1.append((v4, v5))
        v6 = []
        v7 = 0
        for v8, v9 in v1:
            while v6 and v6[0][0] + 2 < v8:
                v7 = max(v7, v6.pop(0)[1])
            v10 = v7 + v9
            v6.append([v8, v10])
        return max((dmg for v11, v12 in v6))
