class C1:

    def numberOfWays(self, a1):
        v1 = 10 ** 9 + 7

        def count_ways(a1):
            if a1 < 0:
                return 0
            v1 = a1 // 6
            v2 = a1 // 2
            v3 = (v2 + 1) * (v1 + 1)
            v4 = 3 * v1 * (v1 + 1) // 2
            return (v3 - v4) % v1
        v2 = 0
        for v3 in range(3):
            v4 = a1 - v3 * 4
            v2 = (v2 + count_ways(v4)) % v1
        return v2
