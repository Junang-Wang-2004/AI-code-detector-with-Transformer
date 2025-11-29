class C1(object):

    def numberOfCleanRooms(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = len(a1[0])
        v3 = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        v4 = v5 = v6 = v7 = 0
        while True:
            v8 = 1 << v7 + 1
            if a1[v5][v6] & v8:
                return v4
            if a1[v5][v6] & ~1 == 0:
                v4 += 1
            a1[v5][v6] |= v8
            v9, v10 = v3[v7]
            v11, v12 = (v5 + v9, v6 + v10)
            if 0 <= v11 < v1 and 0 <= v12 < v2 and (a1[v11][v12] % 2 == 0):
                v5, v6 = (v11, v12)
            else:
                v7 = (v7 + 1) % 4
