class C1(object):

    def splitString(self, a1):
        """
        """

        def backtracking(a1, a2, a3, a4):
            if a2 == len(a1):
                return a4 >= 2
            v1 = 0
            for v2 in range(a2, len(a1)):
                v1 = v1 * 10 + int(a1[v2])
                if v1 >= a3 >= 0:
                    break
                if (a3 == -1 or a3 - 1 == v1) and backtracking(a1, v2 + 1, v1, a4 + 1):
                    return True
            return False
        return backtracking(a1, 0, -1, 0)
