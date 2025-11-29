class C1(object):

    def sortedArrayToBST(self, a1):
        """
        """
        self.iterator = iter(a1)
        return self.helper(0, len(a1))

    def helper(self, a1, a2):
        if a1 == a2:
            return None
        v1 = (a1 + a2) // 2
        v2 = self.helper(a1, v1)
        v3 = TreeNode(next(self.iterator))
        v3.left = v2
        v3.right = self.helper(v1 + 1, a2)
        return v3
