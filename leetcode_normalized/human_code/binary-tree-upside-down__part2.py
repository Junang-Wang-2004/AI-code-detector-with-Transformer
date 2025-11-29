class C1(object):

    def upsideDownBinaryTree(self, a1):
        return self.upsideDownBinaryTreeRecu(a1, None)

    def upsideDownBinaryTreeRecu(self, a1, a2):
        if a1 is None:
            return a2
        v1 = self.upsideDownBinaryTreeRecu(a1.left, a1)
        if a2:
            a1.left = a2.right
        else:
            a1.left = None
        a1.right = a2
        return v1
