class C1:

    def getSum(self, a1):
        v1 = 10 ** 9 + 7

        def calc(a1):
            v1 = {}
            v2 = {}
            v3 = 0
            for v4 in a1:
                v5 = v4 - a1
                v6 = v1.get(v5, 0)
                v7 = (v6 + 1) % v1
                v8 = (v2.get(v5, 0) + v4 * v7) % v1
                v1[v4] = (v1.get(v4, 0) + v7) % v1
                v2[v4] = (v2.get(v4, 0) + v8) % v1
                v3 = (v3 + v8) % v1
            return v3
        v2 = calc(1)
        v3 = calc(-1)
        v4 = sum(a1) % v1
        return (v2 + v3 - v4 + v1) % v1
