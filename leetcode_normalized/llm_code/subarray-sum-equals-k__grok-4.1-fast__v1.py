class C1:

    def subarraySum(self, a1, a2):
        v1 = 0
        v2 = 0
        v3 = {0: 1}
        for v4 in a1:
            v2 += v4
            v1 += v3.get(v2 - a2, 0)
            v3[v2] = v3.get(v2, 0) + 1
        return v1
