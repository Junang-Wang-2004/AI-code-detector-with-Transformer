class C1(object):

    def maxSum(self, a1, a2, a3):
        v1 = len(a1)
        if v1 < a3:
            return 0
        v2 = 0
        v3 = 0
        v4 = 0
        v5 = {}
        for v6 in range(a3):
            v7 = a1[v6]
            v3 += v7
            if v7 not in v5:
                v5[v7] = 1
                v4 += 1
            else:
                v5[v7] += 1
        if v4 >= a2:
            v2 = v3
        for v6 in range(a3, v1):
            v7 = a1[v6]
            v3 += v7
            if v7 not in v5:
                v5[v7] = 1
                v4 += 1
            else:
                v5[v7] += 1
            v8 = a1[v6 - a3]
            v5[v8] -= 1
            if v5[v8] == 0:
                v4 -= 1
            v3 -= v8
            if v4 >= a2:
                v2 = max(v2, v3)
        return v2
