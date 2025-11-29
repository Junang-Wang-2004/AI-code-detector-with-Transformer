class C1(object):

    def maximumBeauty(self, a1, a2):
        v1 = sorted(a1)
        v2 = []
        v3 = 0
        for v4, v5 in v1:
            v3 = max(v3, v5)
            v2.append(v3)
        v6 = [p[0] for v7 in v1]
        v8 = len(v6)

        def last_leq(a1):
            v1, v2 = (0, v8 - 1)
            v3 = -1
            while v1 <= v2:
                v4 = v1 + (v2 - v1) // 2
                if v6[v4] <= a1:
                    v3 = v4
                    v1 = v4 + 1
                else:
                    v2 = v4 - 1
            return v3
        v9 = []
        for v10 in a2:
            v11 = last_leq(v10)
            v9.append(v2[v11] if v11 >= 0 else 0)
        return v9
