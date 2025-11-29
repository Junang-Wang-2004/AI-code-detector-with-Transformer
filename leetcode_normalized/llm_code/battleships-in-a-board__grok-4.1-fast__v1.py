class C1:

    def countBattleships(self, a1):
        if not a1 or not a1[0]:
            return 0
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = 0
        for v4 in range(v1):
            for v5 in range(v2):
                v6 = a1[v4][v5]
                if v6 == 'X':
                    v7 = v4 == 0 or a1[v4 - 1][v5] != 'X'
                    v8 = v5 == 0 or a1[v4][v5 - 1] != 'X'
                    if v7 and v8:
                        v3 += 1
        return v3
