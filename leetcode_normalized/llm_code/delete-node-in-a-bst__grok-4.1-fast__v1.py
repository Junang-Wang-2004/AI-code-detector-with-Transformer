class C1(object):

    def deleteNode(self, a1, a2):
        if not a1:
            return None
        if a2 < a1.val:
            a1.left = self.deleteNode(a1.left, a2)
        elif a2 > a1.val:
            a1.right = self.deleteNode(a1.right, a2)
        else:
            if a1.left is None:
                return a1.right
            if a1.right is None:
                return a1.left
            v1 = a1.left
            while v1.right:
                v1 = v1.right
            a1.val = v1.val
            a1.left = self.deleteNode(a1.left, v1.val)
        return a1
