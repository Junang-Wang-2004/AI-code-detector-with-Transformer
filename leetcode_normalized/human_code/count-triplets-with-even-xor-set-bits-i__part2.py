class C1(object):

    def tripletCount(self, a1, a2, a3):
        """
        """

        def popcount(a1):
            return bin(a1).count('1')

        def count(a1):
            v1 = sum((popcount(x) & 1 for v2 in a1))
            return [len(a1) - v1, v1]
        v1, v2 = count(a1)
        v3, v4 = count(a2)
        v5, v6 = count(a3)
        return v1 * v3 * v5 + v1 * v4 * v6 + v2 * v3 * v6 + v2 * v4 * v5
