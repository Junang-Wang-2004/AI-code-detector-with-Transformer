class C1(object):

    def findLatestStep(self, a1, a2):
        v1 = len(a1)
        v2 = list(range(v1 + 2))
        v3 = [0] * (v1 + 2)
        v4 = 0
        v5 = -1

        def find(a1):
            v1 = a1
            while v2[v1] != v1:
                v1 = v2[v1]
            v2 = a1
            while v2 != v1:
                v3 = v2[v2]
                v2[v2] = v1
                v2 = v3
            return v1

        def unite(a1, a2):
            nonlocal cnt
            v1 = find(a1)
            v2 = find(a2)
            if v1 == v2:
                return
            v3 = v3[v1]
            v4 = v3[v2]
            if v3 == a2:
                v5 -= 1
            if v4 == a2:
                v5 -= 1
            if v3 < v4:
                v1, v2 = (v2, v1)
            v2[v2] = v1
            v3[v1] += v3[v2]
            if v3[v1] == a2:
                v5 += 1
        for v6 in range(v1):
            v7 = a1[v6]
            v3[v7] = 1
            if a2 == 1:
                v4 += 1
            if v3[v7 - 1] > 0:
                unite(v7 - 1, v7)
            if v3[v7 + 1] > 0:
                unite(v7 + 1, v7)
            if v4 > 0:
                v5 = v6 + 1
        return v5
