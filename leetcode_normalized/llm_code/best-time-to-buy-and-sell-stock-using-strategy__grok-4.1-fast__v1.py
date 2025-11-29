class C1(object):

    def maxProfit(self, a1, a2, a3):
        v1 = len(a1)
        v2 = a3 // 2
        v3 = 0
        v4 = 0
        for v5 in range(v1):
            v3 += a1[v5] * a2[v5]
            if v5 < a3:
                if v5 >= v2:
                    v4 += a1[v5]
            else:
                v4 += a1[v5] * a2[v5]
        v6 = max(v3, v4)
        for v5 in range(a3, v1):
            v4 += a1[v5 - a3] * a2[v5 - a3]
            v4 += a1[v5] - a1[v5 - v2]
            v4 -= a1[v5] * a2[v5]
            v6 = max(v6, v4)
        return v6
