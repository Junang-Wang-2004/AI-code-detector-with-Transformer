class C1(object):

    def maxFreeTime(self, a1, a2, a3, a4):
        v1 = len(a3)
        v2 = []
        if v1 > 0:
            v2.append(a3[0])
            for v3 in range(1, v1):
                v2.append(a3[v3] - a4[v3 - 1])
            v2.append(a1 - a4[-1])
        else:
            v2.append(a1)
        v4 = 0
        v5 = 0
        for v6 in range(len(v2)):
            v5 += v2[v6]
            v4 = max(v4, v5)
            if v6 - a2 >= 0:
                v5 -= v2[v6 - a2]
        return v4
