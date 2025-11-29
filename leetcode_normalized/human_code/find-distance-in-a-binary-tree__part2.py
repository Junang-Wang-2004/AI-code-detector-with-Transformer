class C1(object):

    def findDistance(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2, a3, a4):
            if not a1:
                return -1
            v1 = dfs(a1.left, a2, a3, a4)
            v2 = dfs(a1.right, a2, a3, a4)
            if a1.val in (a2, a3):
                if v1 == v2 == -1:
                    return 0
                a4[0] = v1 + 1 if v1 != -1 else v2 + 1
            if v1 != -1 and v2 != -1:
                a4[0] = v1 + v2 + 2
            elif v1 != -1:
                return v1 + 1
            elif v2 != -1:
                return v2 + 1
            return -1
        v1 = [0]
        dfs(a1, a2, a3, v1)
        return v1[0]
