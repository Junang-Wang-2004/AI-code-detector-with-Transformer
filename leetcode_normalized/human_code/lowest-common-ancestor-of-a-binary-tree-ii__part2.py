class C1(object):

    def lowestCommonAncestor(self, a1, a2, a3):
        """
        """

        def dfs(a1, a2, a3, a4):
            if not a1:
                return 0
            v1 = dfs(a1.left, a2, a3, a4)
            v2 = dfs(a1.right, a2, a3, a4)
            v3 = int(a1 == a2 or a1 == a3)
            if v3 + v1 + v2 == 2 and (not a4[0]):
                a4[0] = a1
            return v3 + v1 + v2
        v1 = [0]
        dfs(a1, a2, a3, v1)
        return v1[0]
