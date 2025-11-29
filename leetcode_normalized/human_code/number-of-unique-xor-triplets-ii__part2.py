class C1(object):

    def uniqueXorTriplets(self, a1):
        """
        """
        v1, v2 = (set([0]), set())
        v3 = 1 << max(a1).bit_length()
        for v4 in a1:
            for v5 in v1:
                v2.add(v4 ^ v5)
            for v5 in a1:
                v1.add(v4 ^ v5)
            if len(v2) == v3:
                break
        return len(v2)
