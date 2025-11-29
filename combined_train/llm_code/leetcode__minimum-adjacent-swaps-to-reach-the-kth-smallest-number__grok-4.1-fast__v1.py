class C1(object):

    def getMinSwaps(self, a1, a2):
        v1 = list(a1)
        v2 = len(v1)
        for v3 in range(a2):
            v4 = v2 - 2
            while v4 >= 0 and v1[v4] >= v1[v4 + 1]:
                v4 -= 1
            if v4 >= 0:
                v5 = v2 - 1
                while v1[v5] <= v1[v4]:
                    v5 -= 1
                v1[v4], v1[v5] = (v1[v5], v1[v4])
                v6, v7 = (v4 + 1, v2 - 1)
                while v6 < v7:
                    v1[v6], v1[v7] = (v1[v7], v1[v6])
                    v6 += 1
                    v7 -= 1
        v8 = v1[:]
        v9 = list(a1)
        v10 = 0
        for v11 in range(v2):
            if v9[v11] == v8[v11]:
                continue
            v12 = v11
            while v9[v12] != v8[v11]:
                v12 += 1
            v10 += v12 - v11
            for v13 in range(v12, v11, -1):
                v9[v13], v9[v13 - 1] = (v9[v13 - 1], v9[v13])
        return v10
