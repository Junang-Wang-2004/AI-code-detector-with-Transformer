class C1(object):

    def maxVacationDays(self, a1, a2):
        if not a2 or not a1:
            return 0
        v1 = len(a2)
        v2 = len(a2[0])
        v3 = [-1] * v1
        v3[0] = 0
        for v4 in range(v2):
            v5 = [-1] * v1
            for v6 in range(v1):
                if v3[v6] == -1:
                    continue
                v5[v6] = max(v5[v6], v3[v6] + a2[v6][v4])
                for v7 in range(v1):
                    if a1[v6][v7]:
                        v5[v7] = max(v5[v7], v3[v6] + a2[v7][v4])
            v3 = v5
        return max(v3)
