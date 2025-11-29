class C1(object):

    def rotatedDigits(self, a1):
        """
        """
        v1 = list(map(int, str(a1)))
        v2, v3 = (set([3, 4, 7]), set([2, 5, 6, 9]))

        def dp(a1, a2, a3, a4, a5):
            if a2 == len(a1):
                return int(a4)
            if (a2, a3, a4) not in a5:
                v1 = 0
                for v2 in range(a1[a2] + 1 if a3 else 10):
                    if v2 in v2:
                        continue
                    v1 += dp(a1, a2 + 1, a3 and v2 == a1[a2], a4 or v2 in v3, a5)
                a5[a2, a3, a4] = v1
            return a5[a2, a3, a4]
        v4 = {}
        return dp(v1, 0, True, False, v4)
