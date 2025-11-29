class C1:

    def subarraysDivByK(self, a1, a2):
        v1 = {0: 1}
        v2 = 0
        v3 = 0
        for v4 in a1:
            v2 = (v2 + v4) % a2
            v3 += v1.get(v2, 0)
            v1[v2] = v1.get(v2, 0) + 1
        return v3
