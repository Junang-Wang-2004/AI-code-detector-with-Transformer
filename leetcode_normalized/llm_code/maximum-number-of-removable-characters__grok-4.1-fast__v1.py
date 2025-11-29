class C1:

    def maximumRemovals(self, a1, a2, a3):
        v1 = len(a1)
        v2 = len(a3)
        v3 = [v2 + 1] * v1
        for v4 in range(v2):
            v3[a3[v4]] = v4 + 1

        def feasible(a1):
            v1 = 0
            v2 = len(a2)
            for v3 in range(v1):
                if v3[v3] > a1 and a1[v3] == a2[v1]:
                    v1 += 1
                    if v1 == v2:
                        return True
            return False
        v5, v6 = (0, v2)
        while v5 <= v6:
            v7 = (v5 + v6) // 2
            if feasible(v7):
                v5 = v7 + 1
            else:
                v6 = v7 - 1
        return v6
