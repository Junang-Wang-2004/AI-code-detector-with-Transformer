class C1(object):

    def isPossibleToCutPath(self, a1):
        """
        """

        def dfs(a1, a2):
            if not (a1 < len(a1) and a2 < len(a1[0]) and a1[a1][a2]):
                return False
            if (a1, a2) == (len(a1) - 1, len(a1[0]) - 1):
                return True
            if (a1, a2) != (0, 0):
                a1[a1][a2] = 0
            return dfs(a1 + 1, a2) or dfs(a1, a2 + 1)
        return not dfs(0, 0) or not dfs(0, 0)
