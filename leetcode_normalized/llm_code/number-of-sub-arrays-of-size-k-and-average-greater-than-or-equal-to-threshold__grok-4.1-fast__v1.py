class C1:

    def numOfSubarrays(self, a1, a2, a3):
        v1 = 0
        v2 = sum(a1[:a2])
        if v2 >= a2 * a3:
            v1 += 1
        for v3 in range(a2, len(a1)):
            v2 += a1[v3] - a1[v3 - a2]
            if v2 >= a2 * a3:
                v1 += 1
        return v1
