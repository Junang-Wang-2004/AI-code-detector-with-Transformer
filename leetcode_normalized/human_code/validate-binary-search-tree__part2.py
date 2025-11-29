class C1(object):

    def isValidBST(self, a1):
        return self.isValidBSTRecu(a1, float('-inf'), float('inf'))

    def isValidBSTRecu(self, a1, a2, a3):
        if a1 is None:
            return True
        return a2 < a1.val and a1.val < a3 and self.isValidBSTRecu(a1.left, a2, a1.val) and self.isValidBSTRecu(a1.right, a1.val, a3)
