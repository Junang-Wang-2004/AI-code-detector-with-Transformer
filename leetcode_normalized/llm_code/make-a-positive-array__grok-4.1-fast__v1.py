class C1:

    def makeArrayPositive(self, a1):
        v1 = 0
        v2 = 10 ** 18 + 42
        v3 = a1[0]
        v4 = v3 + a1[1]
        v5 = 0
        for v6 in range(2, len(a1)):
            v7 = v4 + a1[v6]
            if v7 <= v5:
                v7 = v4 + v2
                v1 += 1
            v5 = max(v5, v3)
            v3 = v4
            v4 = v7
        return v1
