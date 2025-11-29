class C1(object):

    def numberOfPatterns(self, a1, a2):
        """
        """

        def merge(a1, a2):
            return a1 | 1 << a2

        def contain(a1, a2):
            return bool(a1 & 1 << a2)

        def convert(a1, a2):
            return 3 * a1 + a2

        def numberOfPatternsHelper(a1, a2, a3, a4, a5):
            v1 = 0
            if a3 > a2:
                return v1
            if a1 <= a3 <= a2:
                v1 += 1
            v2, v3 = divmod(a5, 3)
            for v4 in range(9):
                if contain(a4, v4):
                    continue
                v5, v6 = divmod(v4, 3)
                if (v2 == v5 and abs(v3 - v6) == 2 or (v3 == v6 and abs(v2 - v5) == 2) or (abs(v2 - v5) == 2 and abs(v3 - v6) == 2)) and (not contain(a4, convert((v2 + v5) // 2, (v3 + v6) // 2))):
                    continue
                v1 += numberOfPatternsHelper(a1, a2, a3 + 1, merge(a4, v4), v4)
            return v1
        v1 = 0
        v1 += 4 * numberOfPatternsHelper(a1, a2, 1, merge(0, 0), 0)
        v1 += 4 * numberOfPatternsHelper(a1, a2, 1, merge(0, 1), 1)
        v1 += numberOfPatternsHelper(a1, a2, 1, merge(0, 4), 4)
        return v1
