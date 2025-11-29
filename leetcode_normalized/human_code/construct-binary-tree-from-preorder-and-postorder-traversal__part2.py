class C1(object):

    def constructFromPrePost(self, a1, a2):
        """
        """

        def constructFromPrePostHelper(a1, a2, a3, a4, a5, a6, a7):
            if a2 >= a3 or a5 >= a6:
                return None
            v1 = TreeNode(a1[a2])
            if a3 - a2 > 1:
                v2 = a7[a1[a2 + 1]] - a5 + 1
                v1.left = constructFromPrePostHelper(a1, a2 + 1, a2 + 1 + v2, a4, a5, a5 + v2, a7)
                v1.right = constructFromPrePostHelper(a1, a2 + 1 + v2, a3, a4, a5 + v2, a6 - 1, a7)
            return v1
        v1 = {}
        for v2, v3 in enumerate(a2):
            v1[v3] = v2
        return constructFromPrePostHelper(a1, 0, len(a1), a2, 0, len(a2), v1)
