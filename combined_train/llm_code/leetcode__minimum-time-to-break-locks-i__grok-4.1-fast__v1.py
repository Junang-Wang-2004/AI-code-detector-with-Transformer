class C1:

    def findMinimumTime(self, a1, a2):
        v1 = len(a1)
        v2 = 10 ** 18 + 5
        v3 = {}

        def rec(a1):
            if a1 in v3:
                return v3[a1]
            if a1 == 0:
                v1 = 0
            else:
                v2 = 0
                v3 = a1
                while v3 > 0:
                    v2 += v3 & 1
                    v3 >>= 1
                v4 = 1 + (v2 - 1) * a2
                v1 = v2
                v5 = a1
                v6 = 0
                while v5 > 0:
                    if v5 & 1:
                        v7 = a1 ^ 1 << v6
                        v8 = rec(v7)
                        v9 = (a1[v6] + v4 - 1) // v4
                        v1 = min(v1, v8 + v9)
                    v5 >>= 1
                    v6 += 1
            v3[a1] = v1
            return v1
        return rec((1 << v1) - 1)
