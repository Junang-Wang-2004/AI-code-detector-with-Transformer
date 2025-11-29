class C1(object):

    def countUnivalSubtrees(self, a1):
        [v1, v2] = self.isUnivalSubtrees(a1, 0)
        return v2

    def isUnivalSubtrees(self, a1, a2):
        if not a1:
            return [True, a2]
        [v1, a2] = self.isUnivalSubtrees(a1.left, a2)
        [v3, a2] = self.isUnivalSubtrees(a1.right, a2)
        if self.isSame(a1, a1.left, v1) and self.isSame(a1, a1.right, v3):
            a2 += 1
            return [True, a2]
        return [False, a2]

    def isSame(self, a1, a2, a3):
        return not a2 or (a3 and a1.val == a2.val)
