class C1:

    def boundaryOfBinaryTree(self, a1):

        def add_leaves(a1, a2):
            if a1 is None:
                return
            if a1.left is None and a1.right is None:
                a2.append(a1.val)
                return
            add_leaves(a1.left, a2)
            add_leaves(a1.right, a2)
        if a1 is None:
            return []
        v1 = [a1.val]
        v2 = a1.left
        while v2 is not None and (v2.left is not None or v2.right is not None):
            v1.append(v2.val)
            v2 = v2.left if v2.left is not None else v2.right
        add_leaves(a1.left, v1)
        add_leaves(a1.right, v1)
        v2 = a1.right
        v3 = []
        while v2 is not None and (v2.left is not None or v2.right is not None):
            v3.append(v2.val)
            v2 = v2.right if v2.right is not None else v2.left
        v1.extend(reversed(v3))
        return v1
