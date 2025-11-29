import collections

class C1(object):

    def minimumTotalCost(self, a1, a2):
        v1 = len(a1)
        v2 = collections.Counter()
        v3 = 0
        v4 = 0
        for v5 in range(v1):
            if a1[v5] == a2[v5]:
                v6 = a1[v5]
                v2[v6] += 1
                v3 += v5
                v4 += 1
        if v4 == 0:
            return 0
        v7 = 0
        v8 = None
        for v9, v10 in v2.items():
            if v10 > v7:
                v7 = v10
                v8 = v9
        v11 = 2 * v7 - v4
        if v11 <= 0:
            return v3
        v12 = []
        for v5 in range(v1):
            v13, v14 = (a1[v5], a2[v5])
            if v13 != v14 and v13 != v8 and (v14 != v8):
                v12.append(v5)
        if len(v12) < v11:
            return -1
        v12.sort()
        v15 = sum(v12[:v11])
        return v3 + v15
