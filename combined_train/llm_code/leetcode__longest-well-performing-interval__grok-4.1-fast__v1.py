class C1(object):

    def longestWPI(self, a1):
        v1 = len(a1)
        v2 = v1
        v3 = v1 + 1
        v4 = [v3] * (2 * v1 + 1)
        v4[v2] = -1
        v5 = 0
        v6 = 0
        for v7, v8 in enumerate(a1):
            if v8 > 8:
                v6 += 1
            else:
                v6 -= 1
            if v6 > 0:
                v5 = max(v5, v7 + 1)
            v9 = v6 - 1
            v10 = v2 + v9
            if 0 <= v10 < len(v4) and v4[v10] < v3:
                v5 = max(v5, v7 - v4[v10])
            v11 = v2 + v6
            if v4[v11] == v3:
                v4[v11] = v7
        return v5
