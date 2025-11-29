class C1(object):

    def countQuadruples(self, a1, a2):
        v1 = [-1] * 26
        for v2, v3 in enumerate(a1):
            v4 = ord(v3) - ord('a')
            if v1[v4] == -1:
                v1[v4] = v2
        v5 = [-1] * 26
        for v2, v3 in enumerate(a2):
            v4 = ord(v3) - ord('a')
            v5[v4] = v2
        v6 = []
        for v4 in range(26):
            if v1[v4] != -1 and v5[v4] != -1:
                v6.append(v1[v4] - v5[v4])
        if not v6:
            return 0
        v7 = min(v6)
        return v6.count(v7)
