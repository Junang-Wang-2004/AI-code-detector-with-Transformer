class C1:

    def getLonelyNodes(self, a1):
        v1 = []

        def traverse(a1):
            if not a1:
                return
            if a1.left:
                if not a1.right:
                    v1.append(a1.left.val)
                traverse(a1.left)
            if a1.right:
                if not a1.left:
                    v1.append(a1.right.val)
                traverse(a1.right)
        traverse(a1)
        return v1
