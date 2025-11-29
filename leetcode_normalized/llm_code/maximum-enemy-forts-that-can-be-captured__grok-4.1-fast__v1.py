class C1:

    def captureForts(self, a1):
        v1 = 0
        v2 = -1
        v3 = 0
        for v4 in range(len(a1)):
            if a1[v4] != 0:
                if v2 >= 0 and a1[v4] == -v3:
                    v1 = max(v1, v4 - v2 - 1)
                v2 = v4
                v3 = a1[v4]
        return v1
