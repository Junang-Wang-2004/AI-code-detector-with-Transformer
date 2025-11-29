class C1:

    def alternatingSubarray(self, a1):
        v1 = -1
        v2 = 0
        v3 = 0
        v4 = len(a1)
        for v5 in range(1, v4):
            v6 = a1[v5] - a1[v5 - 1]
            if v6 != 1 and v6 != -1:
                v2 = 0
                continue
            if v2 == 0:
                if v6 == 1:
                    v2 = 2
                    v3 = -1
            elif v6 == v3:
                v2 += 1
                v3 = -v3
            else:
                v2 = 0
                if v6 == 1:
                    v2 = 2
                    v3 = -1
            if v2 >= 2:
                v1 = max(v1, v2)
        return v1
