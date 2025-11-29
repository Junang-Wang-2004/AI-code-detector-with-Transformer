class C1(object):

    def memLeak(self, a1, a2):

        def arith_sum(a1, a2, a3):
            return a3 * (2 * a1 + (a3 - 1) * a2) // 2

        def find_max_count(a1, a2, a3):
            if a3 < 0:
                return 0
            v1, v2 = (0, 2 * 10 ** 9 + 5)
            while v1 < v2:
                v3 = (v1 + v2 + 1) // 2
                if arith_sum(a1, a2, v3) <= a3:
                    v1 = v3
                else:
                    v2 = v3 - 1
            return v1
        v1, v2 = (a1, a2)
        v3 = v1 < v2
        if v3:
            v1, v2 = (v2, v1)
        v4 = v1 - v2
        v5 = find_max_count(1, 1, v4)
        v1 -= arith_sum(1, 1, v5)
        if v1 == v2:
            v3 = False
        v6 = find_max_count(v5 + 1, 2, v1)
        v7 = find_max_count(v5 + 2, 2, v2)
        v1 -= arith_sum(v5 + 1, 2, v6)
        v2 -= arith_sum(v5 + 2, 2, v7)
        if v3:
            v1, v2 = (v2, v1)
        v8 = v5 + v6 + v7 + 1
        return [v8, v1, v2]
