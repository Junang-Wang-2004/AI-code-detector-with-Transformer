class C1(object):

    def isPossibleToCutPath(self, a1):
        """
        """

        def iter_dfs():
            v1 = [(0, 0)]
            while v1:
                v2, v3 = v1.pop()
                if not (v2 < len(a1) and v3 < len(a1[0]) and a1[v2][v3]):
                    continue
                if (v2, v3) == (len(a1) - 1, len(a1[0]) - 1):
                    return True
                if (v2, v3) != (0, 0):
                    a1[v2][v3] = 0
                v1.append((v2, v3 + 1))
                v1.append((v2 + 1, v3))
            return False
        return not iter_dfs() or not iter_dfs()
