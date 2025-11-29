class C1(object):

    def meetRequirement(self, a1, a2, a3):
        v1 = []
        for v2, v3 in a2:
            v4 = max(0, v2 - v3)
            v5 = min(a1, v2 + v3 + 1)
            v1.append((v4, 1))
            v1.append((v5, -1))
        v1.sort()
        v6 = 0
        v7 = 0
        v8 = 0
        v9 = len(v1)
        v10 = len(a3)
        v11 = 0
        while v11 < v10:
            while v8 < v9 and v1[v8][0] <= v11:
                v7 += v1[v8][1]
                v8 += 1
            if v7 >= a3[v11]:
                v6 += 1
            v11 += 1
        return v6
