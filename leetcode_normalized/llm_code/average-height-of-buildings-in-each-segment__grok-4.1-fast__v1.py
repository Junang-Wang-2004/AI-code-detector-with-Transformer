class C1:

    def averageHeightOfBuildings(self, a1):
        v1 = []
        for v2, v3, v4 in a1:
            v1.append((v2, 1, v4))
            v1.append((v3, -1, v4))
        v1.sort()
        v5 = []
        v6 = 0
        v7 = 0
        v8 = None
        for v9, v10, v11 in v1:
            if v7 > 0 and v8 is not None and (v9 > v8):
                v12 = v6 // v7
                v5.append([v8, v9, v12])
            v6 += v10 * v11
            v7 += v10
            v8 = v9
        if not v5:
            return []
        v13 = [v5[0][:]]
        for v14 in v5[1:]:
            v15, v16 = (v13[-1][1], v13[-1][2])
            if v15 == v14[0] and v16 == v14[2]:
                v13[-1][1] = v14[1]
            else:
                v13.append(v14[:])
        return v13
