class C1(object):

    def numOfUnplacedFruits(self, a1, a2):
        v1 = len(a1)
        v2 = len(a2)
        if v2 == 0:
            return v1
        v3 = [0] * (4 * v2)

        def construct(a1, a2, a3):
            if a2 == a3:
                v3[a1] = a2[a2]
                return
            v1 = (a2 + a3) // 2
            construct(2 * a1, a2, v1)
            construct(2 * a1 + 1, v1 + 1, a3)
            v3[a1] = max(v3[2 * a1], v3[2 * a1 + 1])

        def modify(a1, a2, a3, a4, a5):
            if a2 == a3:
                v3[a1] = a5
                return
            v1 = (a2 + a3) // 2
            if a4 <= v1:
                modify(2 * a1, a2, v1, a4, a5)
            else:
                modify(2 * a1 + 1, v1 + 1, a3, a4, a5)
            v3[a1] = max(v3[2 * a1], v3[2 * a1 + 1])

        def get_max(a1, a2, a3, a4, a5):
            if a5 < a2 or a3 < a4:
                return 0
            if a4 <= a2 and a3 <= a5:
                return v3[a1]
            v1 = (a2 + a3) // 2
            v2 = get_max(2 * a1, a2, v1, a4, a5)
            v3 = get_max(2 * a1 + 1, v1 + 1, a3, a4, a5)
            return max(v2, v3)
        construct(1, 0, v2 - 1)
        v4 = 0
        for v5 in a1:
            v6, v7 = (0, v2 - 1)
            v8 = -1
            while v6 <= v7:
                v9 = (v6 + v7) // 2
                if get_max(1, 0, v2 - 1, 0, v9) >= v5:
                    v8 = v9
                    v7 = v9 - 1
                else:
                    v6 = v9 + 1
            if v8 == -1:
                v4 += 1
            else:
                modify(1, 0, v2 - 1, v8, 0)
        return v4
