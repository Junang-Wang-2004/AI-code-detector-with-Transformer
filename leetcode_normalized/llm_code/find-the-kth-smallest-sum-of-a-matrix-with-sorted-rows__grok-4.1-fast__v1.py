class C1:

    def kthSmallest(self, a1, a2):

        def combos_le(a1, a2, a3, a4):
            if a3 == len(a1):
                return 1
            v1 = 0
            v2 = len(a1[0])
            for v3 in range(v2):
                v4 = a4 - a1[a3][v3]
                if v4 < 0:
                    break
                v5 = combos_le(a1, a2 - v1, a3 + 1, v4)
                if v5 == 0:
                    break
                v1 += v5
                if v1 >= a2:
                    return a2
            return v1
        v1 = len(a1)
        v2 = sum((row[0] for v3 in a1))
        v4 = sum((v3[-1] for v3 in a1))
        while v2 < v4:
            v5 = v2 + (v4 - v2) // 2
            if combos_le(a1, a2, 0, v5) >= a2:
                v4 = v5
            else:
                v2 = v5 + 1
        return v2
