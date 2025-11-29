class C1(object):

    def rotateGrid(self, a1, a2):
        """
        """

        def get_index(a1, a2, a3):
            if a3 < a1 - 1:
                return (a3, 0)
            if a3 < a1 - 1 + (a2 - 1):
                return (a1 - 1, a3 - (a1 - 1))
            if a3 < a1 - 1 + (a2 - 1) + (a1 - 1):
                return (a1 - 1 - (a3 - (a1 - 1 + (a2 - 1))), a2 - 1)
            return (0, a2 - 1 - (a3 - (a1 - 1 + (a2 - 1) + (a1 - 1))))

        def reverse(a1, a2, a3, a4, a5, a6):
            while a5 < a6:
                v1, v2 = get_index(a2, a3, a5)
                v3, v4 = get_index(a2, a3, a6)
                a1[a4 + v1][a4 + v2], a1[a4 + v3][a4 + v4] = (a1[a4 + v3][a4 + v4], a1[a4 + v1][a4 + v2])
                a5 += 1
                a6 -= 1
        v1, v2 = (len(a1), len(a1[0]))
        for v3 in range(min(v1, v2) // 2):
            v4 = 2 * (v1 - 1 + (v2 - 1))
            v5 = a2 % v4
            reverse(a1, v1, v2, v3, 0, v4 - 1)
            reverse(a1, v1, v2, v3, 0, v5 - 1)
            reverse(a1, v1, v2, v3, v5, v4 - 1)
            v1, v2 = (v1 - 2, v2 - 2)
        return a1
