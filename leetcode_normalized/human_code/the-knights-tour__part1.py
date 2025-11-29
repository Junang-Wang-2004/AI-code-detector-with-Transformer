class C1(object):

    def tourOfKnight(self, a1, a2, a3, a4):
        """
        """
        v1 = ((1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1))

        def backtracking(a1, a2, a3):

            def degree(a1):
                v1 = 0
                v2, v3 = a1
                for v4, v5 in v1:
                    v6, v7 = (v2 + v4, v3 + v5)
                    if 0 <= v6 < a1 and 0 <= v7 < a2 and (result[v6][v7] == -1):
                        v1 += 1
                return v1
            if a3 == a1 * a2:
                return True
            v1 = []
            for v2, v3 in v1:
                v4, v5 = (a1 + v2, a2 + v3)
                if 0 <= v4 < a1 and 0 <= v5 < a2 and (result[v4][v5] == -1):
                    v1.append((v4, v5))
            for v4, v5 in sorted(v1, key=degree):
                result[v4][v5] = a3
                if backtracking(v4, v5, a3 + 1):
                    return True
                result[v4][v5] = -1
            return False
        v2 = [[-1] * a2 for v3 in range(a1)]
        v2[a3][a4] = 0
        backtracking(a3, a4, 1)
        return v2
