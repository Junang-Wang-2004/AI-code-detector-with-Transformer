class C1(object):

    def getKthCharacter(self, a1, a2):
        if a1.len == 0:
            return a1.val[a2 - 1]
        v1 = 0
        if a1.left:
            v1 = a1.left.len if a1.left.len > 0 else len(a1.left.val)
        if a2 <= v1:
            return self.getKthCharacter(a1.left, a2)
        return self.getKthCharacter(a1.right, a2 - v1)
