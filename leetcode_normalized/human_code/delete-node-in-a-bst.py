class C1(object):

    def deleteNode(self, a1, a2):
        """
        """
        if not a1:
            return a1
        if a1.val > a2:
            a1.left = self.deleteNode(a1.left, a2)
        elif a1.val < a2:
            a1.right = self.deleteNode(a1.right, a2)
        elif not a1.left:
            v1 = a1.right
            del a1
            return v1
        elif not a1.right:
            v2 = a1.left
            del a1
            return v2
        else:
            v3 = a1.right
            while v3.left:
                v3 = v3.left
            a1.val = v3.val
            a1.right = self.deleteNode(a1.right, v3.val)
        return a1
