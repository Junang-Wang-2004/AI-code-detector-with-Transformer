class C1:

    def kthSmallestProduct(self, a1, a2, a3):

        def count_leq(a1, a2, a3):
            v1 = 0
            v2 = len(a2)
            for v3 in a1:
                if v3 == 0:
                    if a3 >= 0:
                        v1 += v2
                    continue
                v4 = 0
                v5 = v2
                if v3 > 0:
                    v6 = a3 // v3
                    while v4 < v5:
                        v7 = (v4 + v5) // 2
                        if a2[v7] <= v6:
                            v4 = v7 + 1
                        else:
                            v5 = v7
                    v1 += v4
                else:
                    while v4 < v5:
                        v7 = (v4 + v5) // 2
                        if a2[v7] * v3 <= a3:
                            v5 = v7
                        else:
                            v4 = v7 + 1
                    v1 += v2 - v4
            return v1
        v1 = [a1[0] * a2[0], a1[0] * a2[-1], a1[-1] * a2[0], a1[-1] * a2[-1]]
        v2 = min(v1)
        v3 = max(v1)
        while v2 < v3:
            v4 = v2 + (v3 - v2) // 2
            if count_leq(a1, a2, v4) >= a3:
                v3 = v4
            else:
                v2 = v4 + 1
        return v2
