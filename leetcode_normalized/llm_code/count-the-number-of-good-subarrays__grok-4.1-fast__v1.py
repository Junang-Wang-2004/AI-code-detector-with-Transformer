class C1(object):

    def countGood(self, a1, a2):
        v1 = len(a1)
        v2 = v1 * (v1 + 1) // 2
        v3 = {}
        v4 = 0
        v5 = 0
        v6 = 0
        for v7 in range(v1):
            v8 = a1[v7]
            v9 = v3.get(v8, 0)
            v5 += v9
            v3[v8] = v9 + 1
            while v5 >= a2 and v4 <= v7:
                v10 = a1[v4]
                v11 = v3.get(v10, 0)
                v5 -= v11 - 1
                v3[v10] = v11 - 1
                v4 += 1
            v6 += v7 - v4 + 1
        return v2 - v6
