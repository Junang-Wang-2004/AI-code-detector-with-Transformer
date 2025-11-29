class C1(object):

    def getLonelyNodes(self, a1):
        """
        """

        def dfs(a1, a2):
            if not a1:
                return
            if a1.left and (not a1.right):
                a2.append(a1.left.val)
            elif a1.right and (not a1.left):
                a2.append(a1.right.val)
            dfs(a1.left, a2)
            dfs(a1.right, a2)
        v1 = []
        dfs(a1, v1)
        return v1
