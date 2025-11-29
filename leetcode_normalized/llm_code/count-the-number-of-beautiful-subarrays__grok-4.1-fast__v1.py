class C1:

    def beautifulSubarrays(self, a1):
        v1 = {0: 1}
        v2 = 0
        v3 = 0
        for v4 in a1:
            v3 ^= v4
            v2 += v1.get(v3, 0)
            v1[v3] = v1.get(v3, 0) + 1
        return v2
