class C1:

    def countBits(self, a1):
        v1 = [0] * (a1 + 1)
        v2 = 1
        while v2 <= a1:
            for v3 in range(v2):
                if v2 + v3 <= a1:
                    v1[v2 + v3] = v1[v3] + 1
            v2 *= 2
        return v1
