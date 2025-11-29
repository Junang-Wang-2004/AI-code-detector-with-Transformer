class C1:

    def unhappyFriends(self, a1, a2, a3):
        v1 = [[0] * a1 for v2 in range(a1)]
        for v3 in range(a1):
            for v4, v5 in enumerate(a2[v3]):
                v1[v3][v5] = v4
        v6 = [-1] * a1
        for v7, v8 in a3:
            v6[v7] = v8
            v6[v8] = v7
        v9 = 0
        for v10 in range(a1):
            v11 = v6[v10]
            v12 = False
            for v13 in range(a1):
                if v13 == v10 or v13 == v11:
                    continue
                v14 = v1[v10][v13] < v1[v10][v11]
                v15 = v1[v13][v10] < v1[v13][v6[v13]]
                if v14 and v15:
                    v12 = True
                    break
            if v12:
                v9 += 1
        return v9
