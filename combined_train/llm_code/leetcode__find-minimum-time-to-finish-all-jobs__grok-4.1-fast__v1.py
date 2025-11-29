class C1(object):

    def minimumTimeRequired(self, a1, a2):
        v1 = len(a1)
        v2 = (1 << v1) - 1
        v3 = [0] * (1 << v1)
        for v4 in range(1 << v1):
            for v5 in range(v1):
                if v4 & 1 << v5:
                    v3[v4] += a1[v5]

        def feasible(a1):
            v1 = [a2 + 1] * (1 << v1)
            v1[0] = 0
            for v2 in range(1, 1 << v1):
                v3 = v2
                while v3 > 0:
                    if v3[v3] <= a1:
                        v4 = v2 ^ v3
                        v1[v2] = min(v1[v2], v1[v4] + 1)
                    v3 = v3 - 1 & v2
            return v1[v2] <= a2
        v6, v7 = (max(a1), sum(a1))
        while v6 < v7:
            v8 = v6 + (v7 - v6) // 2
            if feasible(v8):
                v7 = v8
            else:
                v6 = v8 + 1
        return v6
