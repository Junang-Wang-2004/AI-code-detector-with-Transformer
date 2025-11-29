class C1(object):

    def numberOfCleanRooms(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2 = v3 = v4 = v5 = 0
        while not a1[v3][v4] & 1 << v5 + 1:
            v2 += a1[v3][v4] >> 1 == 0
            a1[v3][v4] |= 1 << v5 + 1
            v6, v7 = v1[v5]
            v8, v9 = (v3 + v6, v4 + v7)
            if 0 <= v8 < len(a1) and 0 <= v9 < len(a1[0]) and (not a1[v8][v9] & 1):
                v3, v4 = (v8, v9)
            else:
                v5 = (v5 + 1) % 4
        return v2
