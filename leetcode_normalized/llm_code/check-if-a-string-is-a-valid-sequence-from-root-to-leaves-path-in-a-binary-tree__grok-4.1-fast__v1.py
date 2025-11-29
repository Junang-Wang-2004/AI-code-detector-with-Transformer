class C1(object):

    def isValidSequence(self, a1, a2):

        def go(a1, a2):
            if a2 == len(a2) or not a1 or a1.val != a2[a2]:
                return False
            if a2 == len(a2) - 1:
                return a1.left is None and a1.right is None
            return go(a1.left, a2 + 1) or go(a1.right, a2 + 1)
        return go(a1, 0)
