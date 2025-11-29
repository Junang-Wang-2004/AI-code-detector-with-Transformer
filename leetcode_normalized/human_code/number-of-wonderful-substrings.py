class C1(object):

    def wonderfulSubstrings(self, a1):
        """
        """
        v1 = 10
        v2 = [0] * 2 ** v1
        v2[0] = 1
        v3 = v4 = 0
        for v5 in a1:
            v4 ^= 1 << ord(v5) - ord('a')
            v3 += v2[v4]
            v3 += sum((v2[v4 ^ 1 << i] for v6 in range(v1)))
            v2[v4] += 1
        return v3
