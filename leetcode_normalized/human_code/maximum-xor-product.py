class C1(object):

    def maximumXorProduct(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7
        for v2 in reversed(range(a3)):
            v3 = 1 << v2
            if min(a1, a2) & v3 == 0:
                a1, a2 = (a1 ^ v3, a2 ^ v3)
        return a1 % v1 * (a2 % v1) % v1
