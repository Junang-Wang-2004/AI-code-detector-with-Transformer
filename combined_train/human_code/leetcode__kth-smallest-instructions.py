class C1(object):

    def kthSmallestPath(self, a1, a2):
        """
        """

        def nCr(a1, a2):
            if a1 < a2:
                return 0
            if a1 - a2 < a2:
                return nCr(a1, a1 - a2)
            v1 = 1
            for v2 in range(1, a2 + 1):
                v1 *= a1 - v2 + 1
                v1 //= v2
            return v1
        v1, v2 = a1
        v3 = []
        while v1 + v2:
            v4 = nCr(v1 + (v2 - 1), v1)
            if a2 <= v4:
                v2 -= 1
                v3.append('H')
            else:
                a2 -= v4
                v1 -= 1
                v3.append('V')
        return ''.join(v3)
