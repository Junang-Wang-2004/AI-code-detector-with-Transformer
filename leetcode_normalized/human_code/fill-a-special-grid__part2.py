class C1(object):

    def specialGrid(self, a1):
        """
        """

        def divide_and_conquer(a1, a2, a3):
            if a1 == 1:
                result[a2][a3] = idx[0]
                idx[0] += 1
                return
            a1 >>= 1
            for v2, v3 in ((0, a1), (a1, 0), (0, -a1), (-a1, 0)):
                a2, a3 = (a2 + v2, a3 + v3)
                divide_and_conquer(a1, a2, a3)
        v1 = 1 << a1
        v2 = [[0] * v1 for v3 in range(v1)]
        v4 = [0]
        divide_and_conquer(v1, 0, 0)
        return v2
