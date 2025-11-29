class C1(object):

    def maxScore(self, a1, a2):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // a2

        def binary_search_right(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if not a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a2

        def check(a1):
            v1 = v2 = 0
            for v3 in range(len(a1)):
                v4 = ceil_divide(a1, a1[v3]) - v2
                if v4 >= 1:
                    v2 = v4 - 1
                    v1 += 2 * v4 - 1
                elif v3 != len(a1) - 1:
                    v2 = 0
                    v1 += 1
                if v1 > a2:
                    return False
            return True
        return binary_search_right(1, max(a1) * a2, check)
