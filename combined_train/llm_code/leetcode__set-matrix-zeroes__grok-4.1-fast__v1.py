class C1:

    def setZeroes(self, a1):
        if not a1 or not a1[0]:
            return
        v1, v2 = (len(a1), len(a1[0]))
        v3 = False
        v4 = False
        for v5 in range(v2):
            if a1[0][v5] == 0:
                v3 = True
        for v6 in range(v1):
            if a1[v6][0] == 0:
                v4 = True
        for v6 in range(1, v1):
            for v5 in range(1, v2):
                if a1[v6][v5] == 0:
                    a1[v6][0] = 0
                    a1[0][v5] = 0
        for v6 in range(v1 - 1, 0, -1):
            for v5 in range(v2 - 1, 0, -1):
                if a1[v6][0] == 0 or a1[0][v5] == 0:
                    a1[v6][v5] = 0
        if v4:
            for v6 in range(v1):
                a1[v6][0] = 0
        if v3:
            for v5 in range(v2):
                a1[0][v5] = 0
