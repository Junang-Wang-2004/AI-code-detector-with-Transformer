class C1:

    def lowestCommonAncestor(self, a1, a2, a3):
        if a1 is None or a1 == a2 or a1 == a3:
            return a1
        v1 = self.lowestCommonAncestor(a1.left, a2, a3)
        v2 = self.lowestCommonAncestor(a1.right, a2, a3)
        if v1 and v2:
            return a1
        return v1 if v1 else v2
