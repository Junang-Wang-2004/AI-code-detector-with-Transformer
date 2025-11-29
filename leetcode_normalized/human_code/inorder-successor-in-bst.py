class C1(object):

    def inorderSuccessor(self, a1, a2):
        """
        """
        if a2 and a2.right:
            a2 = a2.right
            while a2.left:
                a2 = a2.left
            return a2
        v2 = None
        while a1 and a1 != a2:
            if a1.val > a2.val:
                v2 = a1
                a1 = a1.left
            else:
                a1 = a1.right
        return v2
