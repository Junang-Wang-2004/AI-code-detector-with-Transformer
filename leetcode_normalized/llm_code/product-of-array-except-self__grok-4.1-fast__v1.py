class C1:

    def productExceptSelf(self, a1):
        v1 = len(a1)
        if v1 == 0:
            return []
        v2 = [1] * v1
        for v3 in range(v1 - 2, -1, -1):
            v2[v3] = v2[v3 + 1] * a1[v3 + 1]
        v4 = 1
        for v3 in range(v1):
            v2[v3] *= v4
            v4 *= a1[v3]
        return v2
