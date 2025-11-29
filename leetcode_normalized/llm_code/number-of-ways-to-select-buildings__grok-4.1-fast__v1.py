class C1:

    def numberOfWays(self, a1):
        v1 = v2 = v3 = v4 = v5 = v6 = 0
        for v7 in a1:
            v8 = int(v7)
            if v8 == 0:
                v1 += 1
                v3 += v2
                v5 += v4
            else:
                v2 += 1
                v4 += v1
                v6 += v3
        return v5 + v6
