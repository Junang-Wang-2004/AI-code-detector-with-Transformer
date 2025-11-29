class C1:

    def reinitializePermutation(self, a1):
        v1 = a1 - 1
        v2 = 1 % v1
        v3 = 1
        v4 = 2 % v1
        while v4 != v2:
            v4 = v4 * 2 % v1
            v3 += 1
        return v3
