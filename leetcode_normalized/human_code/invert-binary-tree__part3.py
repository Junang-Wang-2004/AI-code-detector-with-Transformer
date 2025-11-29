class C1(object):

    def invertTree(self, a1):
        if a1 is not None:
            a1.left, a1.right = (self.invertTree(a1.right), self.invertTree(a1.left))
        return a1
