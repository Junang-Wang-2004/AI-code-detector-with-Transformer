class C1:

    def numRookCaptures(self, a1):
        v1 = v2 = 0
        for v3 in range(8):
            for v4 in range(8):
                if a1[v3][v4] == 'R':
                    v1, v2 = (v3, v4)
                    break
            else:
                continue
            break
        v5 = 0
        for v4 in range(v2 + 1, 8):
            v6 = a1[v1][v4]
            if v6 == 'p':
                v5 += 1
                break
            if v6 != '.':
                break
        for v4 in range(v2 - 1, -1, -1):
            v6 = a1[v1][v4]
            if v6 == 'p':
                v5 += 1
                break
            if v6 != '.':
                break
        for v3 in range(v1 + 1, 8):
            v6 = a1[v3][v2]
            if v6 == 'p':
                v5 += 1
                break
            if v6 != '.':
                break
        for v3 in range(v1 - 1, -1, -1):
            v6 = a1[v3][v2]
            if v6 == 'p':
                v5 += 1
                break
            if v6 != '.':
                break
        return v5
