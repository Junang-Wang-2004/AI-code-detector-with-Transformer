class C1(object):

    def countBinaryPalindromes(self, a1):
        if a1 == 0:
            return 1
        v1 = a1.bit_length()
        v2 = 1
        for v3 in range(1, v1):
            v4 = (v3 + 1) // 2
            v2 += 1 << v4 - 1
        v5 = v1 // 2
        v6 = a1 >> v5
        v7 = v1 - v5
        v8 = 1 << v7 - 1
        v2 += v6 - v8
        v9 = v6 >> v7 - v5
        v10 = 0
        for v11 in range(v5):
            if v9 & 1 << v11:
                v10 |= 1 << v5 - 1 - v11
        v12 = v6 << v5 | v10
        if v12 <= a1:
            v2 += 1
        return v2
