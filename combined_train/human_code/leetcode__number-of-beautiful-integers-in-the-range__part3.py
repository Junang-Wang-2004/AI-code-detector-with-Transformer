class C1(object):

    def numberOfBeautifulIntegers(self, a1, a2, a3):
        """
        """

        def f(a1):
            v1 = list(map(int, str(a1)))
            v2 = [[[[[-1] * a3 for v3 in range(2 * len(v1) + 1)] for v3 in range(2)] for v3 in range(2)] for v3 in range(len(v1))]

            def memoization(a1, a2, a3, a4, a5):
                if a1 == len(v1):
                    return int(a2 == a4 == a5 == 0)
                if v2[a1][a2][a3][a4][a5] == -1:
                    v1 = 0
                    for v2 in range((v1[a1] if a3 else 9) + 1):
                        v3 = int(a2 and v2 == 0)
                        v4 = int(a3 and v2 == v1[a1])
                        v5 = a4 + ((1 if v2 % 2 == 0 else -1) if v3 == 0 else 0)
                        v6 = (a5 * 10 + v2) % a3
                        v1 += memoization(a1 + 1, v3, v4, v5, v6)
                    v2[a1][a2][a3][a4][a5] = v1
                return v2[a1][a2][a3][a4][a5]
            return memoization(0, 1, 1, 0, 0)
        return f(a2) - f(a1 - 1)
