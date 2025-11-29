class C1(object):

    def findPath(self, a1, a2):
        """
        """
        v1 = ((1, 0), (0, 1), (-1, 0), (0, -1))

        def backtracking(a1, a2, a3):
            v1 = a1[a1][a2]
            if v1 and v1 != a3:
                return False
            a1[a1][a2] = -1
            result.append([a1, a2])
            if len(result) == len(a1) * len(a1[0]):
                return True
            v2 = a3 + 1 if v1 == a3 else a3
            for v3, v4 in v1:
                v5, v6 = (a1 + v3, a2 + v4)
                if not (0 <= v5 < len(a1) and 0 <= v6 < len(a1[0]) and (a1[v5][v6] != -1)):
                    continue
                if backtracking(v5, v6, v2):
                    return True
            result.pop()
            a1[a1][a2] = v1
            return False
        v2 = []
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                if backtracking(v3, v4, 1):
                    return v2
        return v2
