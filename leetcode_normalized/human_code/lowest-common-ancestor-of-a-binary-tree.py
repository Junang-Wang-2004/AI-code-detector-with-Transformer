class C1(object):

    def lowestCommonAncestor(self, a1, a2, a3):
        if a1 in (None, a2, a3):
            return a1
        v1, v2 = [self.lowestCommonAncestor(child, a2, a3) for v3 in (a1.left, a1.right)]
        return a1 if v1 and v2 else v1 or v2
