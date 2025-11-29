class C1:

    def shortestToChar(self, a1, a2):
        v1 = len(a1)
        v2 = [v1] * v1
        v3 = -v1
        for v4 in range(v1):
            if a1[v4] == a2:
                v3 = v4
            v2[v4] = min(v2[v4], v4 - v3)
        v5 = v1 * 2
        for v4 in range(v1 - 1, -1, -1):
            if a1[v4] == a2:
                v5 = v4
            v2[v4] = min(v2[v4], v5 - v4)
        return v2
