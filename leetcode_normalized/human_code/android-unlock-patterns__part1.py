class C1(object):

    def numberOfPatterns(self, a1, a2):
        """
        """

        def merge(a1, a2):
            return a1 | 1 << a2

        def number_of_keys(a1):
            v1 = 0
            while a1 > 0:
                a1 &= a1 - 1
                v1 += 1
            return v1

        def contain(a1, a2):
            return bool(a1 & 1 << a2)

        def convert(a1, a2):
            return 3 * a1 + a2
        v1 = [[0] * 9 for v2 in range(1 << 9)]
        for v3 in range(9):
            v1[merge(0, v3)][v3] = 1
        v4 = 0
        for v5 in range(len(v1)):
            v6 = number_of_keys(v5)
            if v6 > a2:
                continue
            for v3 in range(9):
                if not contain(v5, v3):
                    continue
                if a1 <= v6 <= a2:
                    v4 += v1[v5][v3]
                v7, v8 = divmod(v3, 3)
                for v9 in range(9):
                    if contain(v5, v9):
                        continue
                    v10, v11 = divmod(v9, 3)
                    if (v7 == v10 and abs(v8 - v11) == 2 or (v8 == v11 and abs(v7 - v10) == 2) or (abs(v7 - v10) == 2 and abs(v8 - v11) == 2)) and (not contain(v5, convert((v7 + v10) // 2, (v8 + v11) // 2))):
                        continue
                    v1[merge(v5, v9)][v9] += v1[v5][v3]
        return v4
