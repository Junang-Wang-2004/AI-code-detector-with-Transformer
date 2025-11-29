class C1(object):

    def maxStudents(self, a1):
        """
        """
        v1 = [(-1, -1), (0, -1), (1, -1), (-1, 1), (0, 1), (1, 1)]

        def dfs(a1, a2, a3, a4):
            v1, v2 = a2
            for v3, v4 in v1:
                v5, v6 = (v1 + v3, v2 + v4)
                if 0 <= v5 < len(a1) and 0 <= v6 < len(a1[0]) and (a1[v5][v6] == '.') and (not a3[v5][v6]):
                    a3[v5][v6] = True
                    if a4[v5][v6] == -1 or dfs(a1, a4[v5][v6], a3, a4):
                        a4[v5][v6] = a2
                        return True
            return False

        def Hungarian(a1):
            v1 = 0
            v2 = [[-1] * len(a1[0]) for v3 in range(len(a1))]
            for v4 in range(len(a1)):
                for v5 in range(0, len(a1[0]), 2):
                    if a1[v4][v5] != '.':
                        continue
                    v6 = [[False] * len(a1[0]) for v3 in range(len(a1))]
                    if dfs(a1, (v4, v5), v6, v2):
                        v1 += 1
            return v1
        v2 = 0
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                if a1[v3][v4] == '.':
                    v2 += 1
        return v2 - Hungarian(a1)
