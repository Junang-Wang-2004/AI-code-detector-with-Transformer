class C1(object):

    def maxAreaOfIsland(self, a1):
        """
        """
        v1 = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(a1, a2, a3, a4):
            if not (0 <= a1 < len(a3) and 0 <= a2 < len(a3[0]) and (a3[a1][a2] > 0)):
                return False
            a3[a1][a2] *= -1
            a4[0] += 1
            for v1 in v1:
                dfs(a1 + v1[0], a2 + v1[1], a3, a4)
            return True
        v2 = 0
        for v3 in range(len(a1)):
            for v4 in range(len(a1[0])):
                v5 = [0]
                if dfs(v3, v4, a1, v5):
                    v2 = max(v2, v5[0])
        return v2
