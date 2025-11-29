class C1:

    def countNicePairs(self, a1):
        v1 = 10 ** 9 + 7

        def reverse_num(a1):
            return int(str(a1)[::-1])
        v2 = {}
        for v3 in a1:
            v4 = v3 - reverse_num(v3)
            v2[v4] = v2.get(v4, 0) + 1
        v5 = 0
        for v6 in v2.values():
            v5 = (v5 + v6 * (v6 - 1) // 2) % v1
        return v5
