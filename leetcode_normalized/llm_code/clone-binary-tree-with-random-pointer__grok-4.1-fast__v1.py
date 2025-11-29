class C1:

    def copyRandomBinaryTree(self, a1):
        v1 = {}

        def construct(a1):
            if not a1:
                return None
            if a1 in v1:
                return v1[a1]
            v1 = NodeCopy(a1.val)
            v1[a1] = v1
            v1.left = construct(a1.left)
            v1.right = construct(a1.right)
            v1.random = construct(a1.random)
            return v1
        return construct(a1)
