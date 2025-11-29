class C1:

    def inorderSuccessor(self, a1, a2):
        if a2 and a2.right:
            v1 = a2.right
            while v1.left:
                v1 = v1.left
            return v1
        v2 = None
        v1 = a1
        while v1:
            if a2.val < v1.val:
                v2 = v1
                v1 = v1.left
            else:
                v1 = v1.right
        return v2
