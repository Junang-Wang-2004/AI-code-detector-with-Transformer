class C1:

    def superPow(self, a1, a2):
        v1 = 1337
        v2 = 0
        for v3 in a2:
            v2 = v2 * 10 + v3
        return pow(a1, v2, v1)
