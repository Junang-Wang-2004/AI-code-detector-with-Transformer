class C1(object):

    def splitArray(self, a1):
        v1 = len(a1)
        v2 = 0
        while v2 < v1 - 1 and a1[v2] < a1[v2 + 1]:
            v2 += 1
        v3 = 0
        for v4 in range(v2):
            v3 += a1[v4]
        v5 = v1 - 1
        while v5 > 0 and a1[v5] < a1[v5 - 1]:
            v5 -= 1
        v6 = 0
        for v4 in range(v5 + 1, v1):
            v6 += a1[v4]
        v7 = v5 - v2 + 1
        if v7 >= 3:
            return -1
        if v7 == 2:
            return abs(v3 + a1[v2] - (a1[v5] + v6))
        return min(abs(v3 + a1[v2] - v6), abs(v3 - (a1[v2] + v6)))
