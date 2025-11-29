class C1(object):

    def constructDistancedSequence(self, a1):
        """
        """

        def backtracking(a1, a2, a3, a4):
            if a2 == len(a3):
                return True
            if a3[a2]:
                return backtracking(a1, a2 + 1, a3, a4)
            for v1 in reversed(range(1, a1 + 1)):
                v2 = a2 if v1 == 1 else a2 + v1
                if a4[v1] or v2 >= len(a3) or a3[v2]:
                    continue
                a3[a2], a3[v2], a4[v1] = (v1, v1, True)
                if backtracking(a1, a2 + 1, a3, a4):
                    return True
                a3[a2], a3[v2], a4[v1] = (0, 0, False)
            return False
        v1, v2 = ([0] * (2 * a1 - 1), [False] * (a1 + 1))
        backtracking(a1, 0, v1, v2)
        return v1
