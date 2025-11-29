class C1(object):

    def onceTwice(self, a1):
        """
        """
        v1 = [0] * 3
        v1[0] = ~0
        for v2 in a1:
            v1 = [v2 & v1[i - 1] | ~v2 & v1[i] for v3 in range(3)]
        v4 = [0] * 3
        v4[0] = ~0
        for v2 in a1:
            if ~v2 & v1[1] or v2 & v1[2]:
                continue
            v4 = [v2 & v4[v3 - 1] | ~v2 & v4[v3] for v3 in range(3)]
        return [v4[1], v4[1] ^ v1[1] | v1[2]]
