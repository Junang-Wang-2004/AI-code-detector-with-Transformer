class C1:

    def canCompleteCircuit(self, a1, a2):
        v1 = len(a1)
        v2 = 0
        v3 = 0
        v4 = -1
        v5 = 0
        for v6 in range(v1):
            v7 = a1[v6] - a2[v6]
            v5 += v7
            v2 += v7
            if v2 < v3:
                v3 = v2
                v4 = v6
        if v5 < 0:
            return -1
        return (v4 + 1) % v1
