class C1(object):

    def minNumberOfSeconds(self, a1, a2):
        """
        """

        def binary_search(a1, a2, a3):
            while a1 <= a2:
                v1 = a1 + (a2 - a1) // 2
                if a3(v1):
                    a2 = v1 - 1
                else:
                    a1 = v1 + 1
            return a1

        def check(a1):
            return sum((int((-1 + (1 + 8 * a1 / t) ** 0.5) / 2) for v1 in a2)) >= a1
        v1 = min(a2)
        v2, v3 = (v1, v1 * (a1 + 1) * a1 // 2)
        return binary_search(v2, v3, check)
