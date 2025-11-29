class C1(object):

    def minSkips(self, a1, a2, a3):
        v1 = len(a1)
        v2 = 10 ** 18 + 5
        v3 = [v2] * v1
        v3[0] = 0
        for v4 in range(v1):
            v5 = a1[v4]
            v6 = [v2] * v1
            for v7 in range(v1):
                if v3[v7] == v2:
                    continue
                if v4 < v1 - 1:
                    v8 = (v3[v7] + v5 + a2 - 1) // a2 * a2
                    v6[v7] = min(v6[v7], v8)
                else:
                    v8 = v3[v7] + v5
                    v6[v7] = min(v6[v7], v8)
                if v7 + 1 < v1:
                    v9 = v3[v7] + v5
                    v6[v7 + 1] = min(v6[v7 + 1], v9)
            v3 = v6
        v10 = a3 * a2
        for v7 in range(v1):
            if v3[v7] <= v10:
                return v7
        return -1
