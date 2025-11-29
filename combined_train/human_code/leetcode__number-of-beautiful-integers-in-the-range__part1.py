class C1(object):

    def numberOfBeautifulIntegers(self, a1, a2, a3):
        """
        """
        v1, v2, v3 = list(range(3))

        def f(a1):
            v1 = list(map(int, str(a1)))
            v2 = [[[[-1] * a3 for v3 in range(2 * len(v1) + 1)] for v3 in range(3)] for v3 in range(len(v1))]

            def memoization(a1, a2, a3, a4):
                if a1 == len(v1):
                    return int(a2 != v3 and a3 == a4 == 0)
                if v2[a1][a2][a3][a4] == -1:
                    v1 = int(a1 != 0 and a3 == a4 == 0)
                    for v2 in range(1 if a1 == 0 else 0, 10):
                        v3 = a2
                        if a2 == v1 and v2 != v1[a1]:
                            v3 = v2 if v2 < v1[a1] else v3
                        v4 = a3 + (1 if v2 % 2 == 0 else -1)
                        v5 = (a4 * 10 + v2) % a3
                        v1 += memoization(a1 + 1, v3, v4, v5)
                    v2[a1][a2][a3][a4] = v1
                return v2[a1][a2][a3][a4]
            return memoization(0, v1, 0, 0)
        return f(a2) - f(a1 - 1)
