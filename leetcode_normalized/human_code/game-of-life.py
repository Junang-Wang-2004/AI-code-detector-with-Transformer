class C1(object):

    def gameOfLife(self, a1):
        """
        """
        v1 = len(a1)
        v2 = len(a1[0]) if v1 else 0
        for v3 in range(v1):
            for v4 in range(v2):
                v5 = 0
                for v6 in range(max(v3 - 1, 0), min(v3 + 2, v1)):
                    for v7 in range(max(v4 - 1, 0), min(v4 + 2, v2)):
                        v5 += a1[v6][v7] & 1
                if v5 == 4 and a1[v3][v4] or v5 == 3:
                    a1[v3][v4] |= 2
        for v3 in range(v1):
            for v4 in range(v2):
                a1[v3][v4] >>= 1
