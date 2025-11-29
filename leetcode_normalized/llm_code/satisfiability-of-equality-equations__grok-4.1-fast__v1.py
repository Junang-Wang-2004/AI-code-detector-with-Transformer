class C1:

    def equationsPossible(self, a1):
        v1 = [[False] * 26 for v2 in range(26)]
        for v3 in a1:
            v4 = ord(v3[0]) - ord('a')
            v5 = ord(v3[3]) - ord('a')
            if v3[1] == '!':
                if v4 == v5:
                    return False
            else:
                v1[v4][v5] = True
                v1[v5][v4] = True
        for v6 in range(26):
            for v7 in range(26):
                for v8 in range(26):
                    if v1[v7][v6] and v1[v6][v8]:
                        v1[v7][v8] = True
        for v3 in a1:
            if v3[1] == '!':
                v4 = ord(v3[0]) - ord('a')
                v5 = ord(v3[3]) - ord('a')
                if v1[v4][v5]:
                    return False
        return True
