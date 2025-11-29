class C1(object):

    def flipEquiv(self, a1, a2):
        """
        """
        if not a1 and (not a2):
            return True
        if not a1 or not a2 or a1.val != a2.val:
            return False
        return self.flipEquiv(a1.left, a2.left) and self.flipEquiv(a1.right, a2.right) or (self.flipEquiv(a1.left, a2.right) and self.flipEquiv(a1.right, a2.left))
