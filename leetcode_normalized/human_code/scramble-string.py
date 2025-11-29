class C1(object):

    def isScramble(self, a1, a2):
        if not a1 or not a2 or len(a1) != len(a2):
            return False
        if a1 == a2:
            return True
        v1 = [[[False for v2 in range(len(a2))] for v3 in range(len(a1))] for v4 in range(len(a1) + 1)]
        for v3 in range(len(a1)):
            for v2 in range(len(a2)):
                if a1[v3] == a2[v2]:
                    v1[1][v3][v2] = True
        for v4 in range(2, len(a1) + 1):
            for v3 in range(len(a1) - v4 + 1):
                for v2 in range(len(a2) - v4 + 1):
                    for v5 in range(1, v4):
                        if v1[v5][v3][v2] and v1[v4 - v5][v3 + v5][v2 + v5] or (v1[v5][v3][v2 + v4 - v5] and v1[v4 - v5][v3 + v5][v2]):
                            v1[v4][v3][v2] = True
                            break
        return v1[v4][0][0]
