class C1:

    def kthSmallest(self, a1, a2):

        def count_le(a1):
            v1 = 0
            for v2 in a1:
                v3, v4 = (0, len(v2) - 1)
                while v3 <= v4:
                    v5 = (v3 + v4) // 2
                    if v2[v5] <= a1:
                        v3 = v5 + 1
                    else:
                        v4 = v5 - 1
                v1 += v3
            return v1
        v1, v2 = (a1[0][0], a1[-1][-1])
        while v1 < v2:
            v3 = (v1 + v2) // 2
            if count_le(v3) >= a2:
                v2 = v3
            else:
                v1 = v3 + 1
        return v1
