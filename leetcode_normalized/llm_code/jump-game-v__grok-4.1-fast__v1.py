class C1(object):

    def maxJumps(self, a1, a2):
        v1 = len(a1)
        if v1 == 0:
            return 0
        v2 = [0] * (4 * v1)

        def seg_update(a1, a2, a3=1, a4=0, a5=v1 - 1):
            if a4 == a5:
                v2[a3] = a2
                return
            v1 = (a4 + a5) // 2
            if a1 <= v1:
                seg_update(a1, a2, a3 * 2, a4, v1)
            else:
                seg_update(a1, a2, a3 * 2 + 1, v1 + 1, a5)
            v2[a3] = max(v2[a3 * 2], v2[a3 * 2 + 1])

        def seg_query(a1, a2, a3=1, a4=0, a5=v1 - 1):
            if a1 > a5 or a2 < a4:
                return 0
            if a1 <= a4 and a5 <= a2:
                return v2[a3]
            v1 = (a4 + a5) // 2
            return max(seg_query(a1, a2, a3 * 2, a4, v1), seg_query(a1, a2, a3 * 2 + 1, v1 + 1, a5))
        v3 = sorted(range(v1), key=lambda x: (a1[x], x))
        v4 = 0
        v5 = 1
        while v4 < v1:
            v6 = a1[v3[v4]]
            v7 = []
            while v4 < v1 and a1[v3[v4]] == v6:
                v7.append(v3[v4])
                v4 += 1
            v8 = []
            for v9 in v7:
                v10 = max(0, v9 - a2)
                v11 = min(v1 - 1, v9 + a2)
                v12 = seg_query(v10, v11)
                v13 = 1 + v12
                v8.append(v13)
                v5 = max(v5, v13)
            for v14 in range(len(v7)):
                seg_update(v7[v14], v8[v14])
        return v5
