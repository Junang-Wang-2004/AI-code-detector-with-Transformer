class C1(object):

    def cloneTree(self, a1):
        """
        """

        def dfs(a1):
            if not a1:
                return None
            v1 = Node(a1.val)
            for v2 in a1.children:
                v1.children.append(dfs(v2))
            return v1
        return dfs(a1)
