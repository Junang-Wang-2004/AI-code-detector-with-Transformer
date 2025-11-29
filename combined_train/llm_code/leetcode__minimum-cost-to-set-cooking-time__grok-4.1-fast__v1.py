class C1:

    def minCostSetTime(self, a1, a2, a3, a4):

        def calc_cost(a1, a2, a3, a4, a5):
            if a4 < 0 or a4 > 99 or a5 > 99:
                return float('inf')
            v1 = a4 * 100 + a5
            v2 = []
            if v1 == 0:
                v2 = [0]
            else:
                v3 = v1
                while v3:
                    v2.append(v3 % 10)
                    v3 //= 10
                v2.reverse()
            v4 = 0
            v5 = a1
            for v6 in v2:
                if v6 != v5:
                    v4 += a2
                v4 += a3
                v5 = v6
            return v4
        v1, v2 = divmod(a4, 60)
        v3 = calc_cost(a1, a2, a3, v1, v2)
        v4 = calc_cost(a1, a2, a3, v1 - 1, v2 + 60)
        return min(v3, v4)
