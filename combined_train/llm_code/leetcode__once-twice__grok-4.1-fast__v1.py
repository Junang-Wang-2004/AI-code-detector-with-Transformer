class C1:

    def onceTwice(self, a1):
        v1, v2 = (0, 0)
        for v3 in a1:
            v2 |= v1 & v3
            v1 ^= v3
            v4 = v1 & v2
            v1 &= ~v4
            v2 &= ~v4
        v5, v6 = (0, 0)
        for v3 in a1:
            if v3 & v1 != v1 or v3 & v2:
                continue
            v6 |= v5 & v3
            v5 ^= v3
            v7 = v5 & v6
            v5 &= ~v7
            v6 &= ~v7
        v8 = v5 ^ v1 | v2
        return [v5, v8]
