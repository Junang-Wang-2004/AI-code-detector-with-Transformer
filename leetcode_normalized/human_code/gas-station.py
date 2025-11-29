class C1(object):

    def canCompleteCircuit(self, a1, a2):
        v1, v2, v3 = (0, 0, 0)
        for v4 in range(len(a1)):
            v5 = a1[v4] - a2[v4]
            v3 += v5
            v2 += v5
            if v3 < 0:
                v1 = v4 + 1
                v3 = 0
        if v2 >= 0:
            return v1
        return -1
