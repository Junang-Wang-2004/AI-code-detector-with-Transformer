class C1:

    def numSubarrayProductLessThanK(self, a1, a2):
        if a2 <= 1:
            return 0
        v1 = 0
        v2 = 0
        v3 = 1
        v4 = len(a1)
        for v5 in range(v4):
            v3 *= a1[v5]
            while v3 >= a2:
                v3 //= a1[v2]
                v2 += 1
            v1 += v5 - v2 + 1
        return v1
