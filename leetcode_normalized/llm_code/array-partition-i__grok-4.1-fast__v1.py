class C1:

    def arrayPairSum(self, a1):
        v1 = sorted(a1)
        v2 = 0
        v3 = 0
        while v3 < len(v1):
            v2 += v1[v3]
            v3 += 2
        return v2
