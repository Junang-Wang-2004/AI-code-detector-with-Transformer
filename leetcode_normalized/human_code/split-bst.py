class C1(object):

    def splitBST(self, a1, a2):
        """
        """
        if not a1:
            return (None, None)
        elif a1.val <= a2:
            v1 = self.splitBST(a1.right, a2)
            a1.right = v1[0]
            return (a1, v1[1])
        else:
            v1 = self.splitBST(a1.left, a2)
            a1.left = v1[1]
            return (v1[0], a1)
