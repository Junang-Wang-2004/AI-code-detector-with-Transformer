class C1(object):

    def productExceptSelf(self, a1):
        if not a1:
            return []
        v1 = [1 for v2 in range(len(a1))]
        for v3 in range(1, len(a1)):
            v1[v3] = v1[v3 - 1] * a1[v3 - 1]
        v4 = 1
        for v3 in range(len(a1) - 2, -1, -1):
            v4 *= a1[v3 + 1]
            v1[v3] = v1[v3] * v4
        return v1
