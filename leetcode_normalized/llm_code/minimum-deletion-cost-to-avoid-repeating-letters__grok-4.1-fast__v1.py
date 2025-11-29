class C1(object):

    def minCost(self, a1, a2):
        v1 = sum(a2)
        v2 = len(a1)
        v3 = 0
        v4 = 0
        while v3 < v2:
            v5 = a1[v3]
            v6 = 0
            while v3 < v2 and a1[v3] == v5:
                v6 = max(v6, a2[v3])
                v3 += 1
            v4 += v6
        return v1 - v4
