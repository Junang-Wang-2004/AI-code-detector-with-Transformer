class C1(object):

    def decode(self, a1):
        """
        """
        v1 = 0
        for v2 in range(1, len(a1) + 1 + 1):
            v1 ^= v2
            if v2 < len(a1) and v2 % 2 == 1:
                v1 ^= a1[v2]
        v3 = [v1]
        for v4 in a1:
            v3.append(v3[-1] ^ v4)
        return v3
