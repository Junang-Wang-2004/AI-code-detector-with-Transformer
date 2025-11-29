class C1(object):

    def minDays(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def floodfill(a1, a2, a3, a4):
            v1 = [(a2, a3)]
            a4[a2][a3] = 1
            while v1:
                a2, a3 = v1.pop()
                for v4, v5 in v1:
                    v6, v7 = (a2 + v4, a3 + v5)
                    if not (0 <= v6 < R and 0 <= v7 < C and a1[v6][v7] and (not a4[v6][v7])):
                        continue
                    a4[v6][v7] = 1
                    v1.append((v6, v7))

        def count_islands(a1):
            v1 = [[0] * C for v2 in range(R)]
            v3 = 0
            for v4 in range(R):
                for v5 in range(C):
                    if a1[v4][v5] == 0 or v1[v4][v5]:
                        continue
                    v3 += 1
                    floodfill(a1, v4, v5, v1)
            return v3
        v2, v3 = (len(a1), len(a1[0]))
        if count_islands(a1) != 1:
            return 0
        for v4 in range(v2):
            for v5 in range(v3):
                if a1[v4][v5] == 0:
                    continue
                a1[v4][v5] = 0
                v6 = count_islands(a1)
                a1[v4][v5] = 1
                if v6 != 1:
                    return 1
        return 2
