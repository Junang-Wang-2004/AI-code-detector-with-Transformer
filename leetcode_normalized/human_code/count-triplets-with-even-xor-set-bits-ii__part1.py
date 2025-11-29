class C1(object):

    def tripletCount(self, a1, a2, a3):
        """
        """

        def popcount(a1):
            return bin(a1).count('1')

        def count(a1):
            v1 = sum((popcount(x) & 1 for v2 in a1))
            return [len(a1) - v1, v1]
        v1 = list(map(count, (a1, a2, a3)))
        return sum((v1[0][0 if i == 0 or i == 1 else 1] * v1[1][0 if i == 0 or i == 2 else 1] * v1[2][0 if i == 0 or i == 3 else 1] for v2 in range(4)))
