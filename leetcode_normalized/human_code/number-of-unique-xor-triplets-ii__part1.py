class C1(object):

    def uniqueXorTriplets(self, a1):
        """
        """

        def fst(a1, a2):
            v1 = len(a1)
            v2 = 1
            while v2 < v1:
                for v3 in range(0, v1, v2 << 1):
                    for v4 in range(v3, v3 + v2):
                        v5, v6 = (a1[v4], a1[v4 + v2])
                        a1[v4], a1[v4 + v2] = (v5 + v6, v5 - v6)
                v2 <<= 1
            if a2:
                for v3 in range(v1):
                    a1[v3] //= v1
        v1 = [0] * (1 << max(a1).bit_length())
        for v2 in a1:
            v1[v2] += 1
        fst(v1, False)
        for v3 in range(len(v1)):
            v1[v3] = v1[v3] ** 3
        fst(v1, True)
        return sum((v2 != 0 for v2 in v1))
