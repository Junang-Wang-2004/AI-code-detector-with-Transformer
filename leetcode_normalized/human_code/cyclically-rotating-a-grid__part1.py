import fractions

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
        v1, v2 = (len(a1), len(a1[0]))
        for v3 in range(min(v1, v2) // 2):
            v4 = 2 * (v1 - 1 + (v2 - 1))
            v5 = a2 % v4
            v6 = fractions.gcd(v4, v5)
            v7 = v4 // v6
            for v8 in range(v6):
                v9, v10 = get_index(v1, v2, v8)
                for v11 in range(1, v7):
                    v12, v13 = get_index(v1, v2, (v8 + v11 * v5) % v4)
                    a1[v3 + v12][v3 + v13], a1[v3 + v9][v3 + v10] = (a1[v3 + v9][v3 + v10], a1[v3 + v12][v3 + v13])
            v1, v2 = (v1 - 2, v2 - 2)
        return a1
