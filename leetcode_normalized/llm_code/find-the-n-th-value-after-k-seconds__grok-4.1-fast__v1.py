class C1:

    def valueAfterKSeconds(self, a1, a2):
        v1 = 10 ** 9 + 7
        v2 = a1 + a2 - 1
        v3 = min(a2, a1 - 1)
        v4 = 1
        for v5 in range(v3):
            v4 = v4 * (v2 - v5) % v1
            v4 = v4 * pow(v5 + 1, v1 - 2, v1) % v1
        return v4
