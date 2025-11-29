class C1:

    def handleQuery(self, a1, a2, a3):
        v1 = len(a1)
        v2 = sum(a2)
        v3 = []
        v4 = [0] * (4 * v1)
        v5 = [0] * (4 * v1)

        def construct(a1, a2, a3):
            if a2 == a3:
                v4[a1] = a1[a2]
                return
            v1 = (a2 + a3) // 2
            construct(2 * a1, a2, v1)
            construct(2 * a1 + 1, v1 + 1, a3)
            v4[a1] = v4[2 * a1] + v4[2 * a1 + 1]

        def push_down(a1, a2, a3):
            if v5[a1]:
                v4[a1] = a3 - a2 + 1 - v4[a1]
                if a2 != a3:
                    v5[2 * a1] ^= 1
                    v5[2 * a1 + 1] ^= 1
                v5[a1] = 0

        def range_flip(a1, a2, a3, a4, a5):
            push_down(a1, a2, a3)
            if a2 > a3 or a2 > a5 or a3 < a4:
                return
            if a4 <= a2 and a3 <= a5:
                v5[a1] ^= 1
                push_down(a1, a2, a3)
                return
            v1 = (a2 + a3) // 2
            range_flip(2 * a1, a2, v1, a4, a5)
            range_flip(2 * a1 + 1, v1 + 1, a3, a4, a5)
            v4[a1] = v4[2 * a1] + v4[2 * a1 + 1]

        def get_sum(a1, a2, a3, a4, a5):
            push_down(a1, a2, a3)
            if a2 > a3 or a2 > a5 or a3 < a4:
                return 0
            if a4 <= a2 and a3 <= a5:
                return v4[a1]
            v1 = (a2 + a3) // 2
            v2 = get_sum(2 * a1, a2, v1, a4, a5)
            v3 = get_sum(2 * a1 + 1, v1 + 1, a3, a4, a5)
            return v2 + v3
        construct(1, 0, v1 - 1)
        for v6 in a3:
            v7, v8, v9 = v6
            if v7 == 1:
                range_flip(1, 0, v1 - 1, v8, v9)
            elif v7 == 2:
                v10 = get_sum(1, 0, v1 - 1, 0, v1 - 1)
                v2 += v10 * v8
            else:
                v3.append(v2)
        return v3
