class C1(object):

    def separateSquares(self, a1):
        """
        """
        v1 = 1e-05

        def binary_search(a1, a2, a3):
            while a2 - a1 > v1:
                v1 = a1 + (a2 - a1) / 2.0
                if a3(v1):
                    a2 = v1
                else:
                    a1 = v1
            return a1

        def check(a1):
            v1 = 0
            for v2, v3, v4 in a1:
                if v3 >= a1:
                    v1 += v4 ** 2
                elif v3 + v4 <= a1:
                    v1 -= v4 ** 2
                else:
                    v1 += v4 * (v3 + v4 - a1 - (a1 - v3))
            return v1 <= 0
        return binary_search(min((y for v2, v3, v2 in a1)), max((v3 + l for v2, v3, v4 in a1)), check)
