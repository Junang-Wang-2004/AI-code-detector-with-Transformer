class C1:

    def maximumSumSubsequence(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = len(a1)
        v3 = [[0] * 4 for v4 in range(4 * v2)]

        def merge(a1, a2):
            v1 = [0] * 4
            v1[0] = max(a1[2] + a2[1], a1[0] + a2[1], a1[2] + a2[0])
            v1[1] = max(a1[3] + a2[1], a1[1] + a2[1], a1[3] + a2[0])
            v1[2] = max(a1[2] + a2[3], a1[0] + a2[3], a1[2] + a2[2])
            v1[3] = max(a1[3] + a2[3], a1[1] + a2[3], a1[3] + a2[2])
            return v1

        def construct(a1, a2, a3):
            if a2 == a3:
                v1 = max(a1[a2], 0)
                v3[a1] = [v1, 0, 0, 0]
                return
            v2 = (a2 + a3) // 2
            construct(2 * a1, a2, v2)
            construct(2 * a1 + 1, v2 + 1, a3)
            v3[a1] = merge(v3[2 * a1], v3[2 * a1 + 1])

        def modify(a1, a2, a3, a4, a5):
            if a2 == a3:
                a5 = max(a5, 0)
                v3[a1] = [a5, 0, 0, 0]
                return
            v2 = (a2 + a3) // 2
            if a4 <= v2:
                modify(2 * a1, a2, v2, a4, a5)
            else:
                modify(2 * a1 + 1, v2 + 1, a3, a4, a5)
            v3[a1] = merge(v3[2 * a1], v3[2 * a1 + 1])
        construct(1, 0, v2 - 1)
        v5 = 0
        for v6, v7 in a2:
            modify(1, 0, v2 - 1, v6, v7)
            v5 = (v5 + max(v3[1])) % v1
        return v5
