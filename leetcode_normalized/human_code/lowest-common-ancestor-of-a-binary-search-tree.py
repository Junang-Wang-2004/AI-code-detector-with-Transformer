class C1(object):

    def lowestCommonAncestor(self, a1, a2, a3):
        v1, v2 = sorted([a2.val, a3.val])
        while not v1 <= a1.val <= v2:
            a1 = a1.left if v1 <= a1.val else a1.right
        return a1
