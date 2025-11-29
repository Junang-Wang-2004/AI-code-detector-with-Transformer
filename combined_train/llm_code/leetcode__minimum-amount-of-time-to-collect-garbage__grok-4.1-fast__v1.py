class C1:

    def garbageCollection(self, a1, a2):
        v1 = len(a1)
        v2 = [0] * v1
        for v3 in range(1, v1):
            v2[v3] = v2[v3 - 1] + a2[v3 - 1]
        v4 = v5 = v6 = -1
        v7 = 0
        for v3, v8 in enumerate(a1):
            v7 += len(v8)
            for v9 in v8:
                if v9 == 'G':
                    v4 = v3
                elif v9 == 'M':
                    v5 = v3
                elif v9 == 'P':
                    v6 = v3
        v10 = 0
        if v4 >= 0:
            v10 += v2[v4]
        if v5 >= 0:
            v10 += v2[v5]
        if v6 >= 0:
            v10 += v2[v6]
        return v7 + v10
