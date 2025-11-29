class C1(object):

    def insertIntoBST(self, a1, a2):
        """
        """
        if not a1:
            a1 = TreeNode(a2)
        elif a2 <= a1.val:
            a1.left = self.insertIntoBST(a1.left, a2)
        else:
            a1.right = self.insertIntoBST(a1.right, a2)
        return a1
