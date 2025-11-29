class C1:

    def wonderfulSubstrings(self, a1):
        v1 = 1 << 10
        v2 = [0] * v1
        v2[0] = 1
        v3 = 0
        v4 = 0
        for v5 in a1:
            v6 = ord(v5) - ord('a')
            v3 ^= 1 << v6
            v4 += v2[v3]
            for v7 in range(10):
                v8 = v3 ^ 1 << v7
                v4 += v2[v8]
            v2[v3] += 1
        return v4
