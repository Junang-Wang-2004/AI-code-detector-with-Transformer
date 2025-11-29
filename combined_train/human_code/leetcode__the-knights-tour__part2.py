class C1(object):

    def tourOfKnight(self, a1, a2, a3, a4):
        """
        """
        v1 = ((1, 2), (-1, 2), (1, -2), (-1, -2), (2, 1), (-2, 1), (2, -1), (-2, -1))

        def backtracking(a1, a2, a3):
            if a3 == a1 * a2:
                return True
            for v1, v2 in v1:
                v3, v4 = (a1 + v1, a2 + v2)
                if not (0 <= v3 < a1 and 0 <= v4 < a2 and (result[v3][v4] == -1)):
                    continue
                result[v3][v4] = a3
                if backtracking(v3, v4, a3 + 1):
                    return True
                result[v3][v4] = -1
            return False
        v2 = [[-1] * a2 for v3 in range(a1)]
        v2[a3][a4] = 0
        backtracking(a3, a4, 1)
        return v2
