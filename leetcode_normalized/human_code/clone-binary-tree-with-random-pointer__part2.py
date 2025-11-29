class C1(object):

    def copyRandomBinaryTree(self, a1):
        """
        """

        def dfs(a1, a2):
            if not a1:
                return None
            v1, v2 = a2(a1)
            dfs(v1, a2)
            dfs(a1.right, a2)
            return v2

        def merge(a1):
            v1 = NodeCopy(a1.val)
            a1.left, v1.left = (v1, a1.left)
            return (v1.left, v1)

        def clone(a1):
            v1 = a1.left
            a1.left.random = a1.random.left if a1.random else None
            a1.left.right = a1.right.left if a1.right else None
            return (v1.left, v1)

        def split(a1):
            v1 = a1.left
            a1.left, v1.left = (v1.left, v1.left.left if v1.left else None)
            return (a1.left, v1)
        dfs(a1, merge)
        dfs(a1, clone)
        return dfs(a1, split)
