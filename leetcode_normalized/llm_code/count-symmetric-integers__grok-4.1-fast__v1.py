class C1:

    def countSymmetricIntegers(self, a1, a2):

        def is_symmetric(a1):
            v1 = str(a1)
            v2 = len(v1)
            if v2 % 2 != 0:
                return False
            v3 = v2 // 2
            v4 = sum((int(c) for v5 in v1[:v3]))
            v6 = sum((int(v5) for v5 in v1[v3:]))
            return v4 == v6
        v1 = 0
        for v2 in range(a1, a2 + 1):
            if is_symmetric(v2):
                v1 += 1
        return v1
