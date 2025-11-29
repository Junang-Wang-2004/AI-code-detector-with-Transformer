class C1(object):

    def amountOfTime(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3):
            if a1 is None:
                return [-1, -1]
            v1 = dfs(a1.left, a2, a3)
            v2 = dfs(a1.right, a2, a3)
            v3 = -1
            if a1.val == a2:
                v3 = 0
                a3[0] = max(v1[0], v2[0]) + 1
            elif v1[1] >= 0:
                v3 = v1[1] + 1
                a3[0] = max(a3[0], v2[0] + 1 + v3)
            elif v2[1] >= 0:
                v3 = v2[1] + 1
                a3[0] = max(a3[0], v1[0] + 1 + v3)
            return [max(v1[0], v2[0]) + 1, v3]
        v1 = [-1]
        dfs(a1, a2, v1)
        return v1[0]
